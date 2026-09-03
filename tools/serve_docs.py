#!/usr/bin/env python3
"""Live preview server for the GreenShield Plus design workspace.

This repository is a Markdown-only knowledge base (research, prototypes,
design system, delivery). There is no build step and no application to
compile. This small server renders every ``.md`` file to HTML on the fly and
serves it with a navigable sidebar so the workspace can be browsed in a
browser exactly the way it reads on GitHub — no coding required.

Usage::

    python tools/serve_docs.py --host 0.0.0.0 --port 8000 --root .

Only depends on ``markdown`` (see ``tools/requirements.txt``); everything
else is from the Python standard library.
"""

from __future__ import annotations

import argparse
import html
import os
import posixpath
from functools import lru_cache
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlparse

import markdown

# Directories that are never part of the design workspace content.
IGNORED_DIRS = {".git", ".github", "node_modules", "tmp", ".scratch", "__pycache__"}

MD_EXTENSIONS = [
    "extra",        # tables, fenced code, footnotes, etc.
    "toc",
    "sane_lists",
    "admonition",
]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · GreenShield Plus 设计工作台</title>
<style>
  :root {{
    --green: #1f7a4d;
    --green-dark: #145235;
    --bg: #f6f8f7;
    --sidebar-bg: #0f2a1e;
    --sidebar-fg: #cfe6da;
    --border: #e2e8e5;
    --text: #1c2b24;
    --muted: #5b6b63;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
      "Hiragino Sans GB", "Microsoft YaHei", Roboto, Helvetica, Arial, sans-serif;
    color: var(--text);
    background: var(--bg);
    display: flex;
    min-height: 100vh;
  }}
  aside {{
    width: 320px;
    flex: 0 0 320px;
    background: var(--sidebar-bg);
    color: var(--sidebar-fg);
    padding: 20px 16px 48px;
    overflow-y: auto;
    height: 100vh;
    position: sticky;
    top: 0;
  }}
  aside h1 {{
    font-size: 15px;
    color: #fff;
    margin: 4px 8px 16px;
    letter-spacing: .3px;
  }}
  aside a {{ color: var(--sidebar-fg); text-decoration: none; }}
  .tree-dir {{ margin: 10px 0 2px; }}
  .tree-dir > span {{
    display: block;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .6px;
    color: #7fb79a;
    padding: 4px 8px;
  }}
  .tree-file {{
    display: block;
    padding: 5px 8px 5px 20px;
    font-size: 13px;
    border-radius: 6px;
    line-height: 1.35;
  }}
  .tree-file:hover {{ background: rgba(255,255,255,.08); }}
  .tree-file.active {{ background: var(--green); color: #fff; }}
  main {{
    flex: 1 1 auto;
    padding: 40px 56px 96px;
    max-width: 900px;
  }}
  .crumbs {{ color: var(--muted); font-size: 13px; margin-bottom: 18px; }}
  article {{
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 40px 48px;
    box-shadow: 0 1px 2px rgba(20,40,30,.04);
  }}
  article h1, article h2, article h3 {{ color: var(--green-dark); }}
  article h1 {{ margin-top: 0; border-bottom: 2px solid var(--border); padding-bottom: 12px; }}
  article h2 {{ margin-top: 32px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }}
  article code {{
    background: #eef3f0; padding: 2px 6px; border-radius: 4px;
    font-size: 90%; font-family: "SFMono-Regular", Consolas, monospace;
  }}
  article pre {{
    background: #0f2a1e; color: #d7efe3; padding: 16px;
    border-radius: 8px; overflow-x: auto;
  }}
  article pre code {{ background: transparent; color: inherit; padding: 0; }}
  article table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
  article th, article td {{ border: 1px solid var(--border); padding: 8px 12px; text-align: left; }}
  article th {{ background: #eef3f0; }}
  article a {{ color: var(--green); }}
  article blockquote {{
    border-left: 4px solid var(--green); margin: 16px 0; padding: 4px 16px;
    color: var(--muted); background: #f2f7f4;
  }}
  .empty {{ color: var(--muted); font-style: italic; }}
  footer {{ margin-top: 24px; color: var(--muted); font-size: 12px; }}
</style>
</head>
<body>
<aside>
  <h1>🌿 GreenShield Plus<br><span style="font-weight:400;color:#7fb79a;font-size:12px">产品设计工作台</span></h1>
  {nav}
</aside>
<main>
  <div class="crumbs">{crumbs}</div>
  <article>
  {content}
  </article>
  <footer>本地预览 · 由 tools/serve_docs.py 渲染 · 源文件：{relpath}</footer>
</main>
</body>
</html>
"""


def is_hidden_or_ignored(name: str) -> bool:
    return name in IGNORED_DIRS or name.startswith(".")


def build_nav(root: str, current_rel: str) -> str:
    """Build the sidebar navigation grouped by top-level folder."""
    parts: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not is_hidden_or_ignored(d))
        rel_dir = os.path.relpath(dirpath, root)
        md_files = sorted(f for f in filenames if f.endswith(".md"))
        if not md_files:
            continue
        label = "根目录" if rel_dir == "." else rel_dir
        parts.append(f'<div class="tree-dir"><span>{html.escape(label)}</span>')
        for f in md_files:
            rel = "" if rel_dir == "." else rel_dir + "/"
            rel_path = (rel + f).replace(os.sep, "/")
            active = " active" if rel_path == current_rel else ""
            url = "/" + rel_path
            parts.append(
                f'<a class="tree-file{active}" href="{html.escape(url)}">'
                f"{html.escape(f)}</a>"
            )
        parts.append("</div>")
    return "\n".join(parts)


@lru_cache(maxsize=1)
def _md() -> "markdown.Markdown":
    return markdown.Markdown(extensions=MD_EXTENSIONS)


def render_markdown(text: str) -> str:
    md = _md()
    md.reset()
    return md.convert(text)


def make_crumbs(rel_path: str) -> str:
    if not rel_path:
        return "首页"
    segments = rel_path.split("/")
    trail = ['<a href="/">首页</a>']
    for seg in segments[:-1]:
        trail.append(html.escape(seg))
    trail.append(f"<strong>{html.escape(segments[-1])}</strong>")
    return " / ".join(trail)


class DocsHandler(BaseHTTPRequestHandler):
    root = "."

    def log_message(self, fmt, *args):  # noqa: D401 - quieter logging
        print("[serve_docs] " + fmt % args)

    def _send_html(self, body: str, status: int = 200) -> None:
        encoded = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(encoded)

    def _resolve(self, url_path: str) -> str | None:
        """Map a URL path to a safe absolute filesystem path within root."""
        rel = unquote(urlparse(url_path).path).lstrip("/")
        if rel in ("", "/"):
            rel = "README.md"
        norm = posixpath.normpath(rel)
        if norm.startswith("..") or os.path.isabs(norm):
            return None
        abs_path = os.path.join(self.root, norm)
        if os.path.isdir(abs_path):
            abs_path = os.path.join(abs_path, "README.md")
        return abs_path

    def do_HEAD(self) -> None:  # noqa: N802
        self.do_GET()

    def do_GET(self) -> None:  # noqa: N802
        if urlparse(self.path).path == "/healthz":
            self._send_html("ok")
            return

        abs_path = self._resolve(self.path)
        if abs_path is None:
            self._send_html("<h1>400 Bad Request</h1>", status=400)
            return

        rel_path = os.path.relpath(abs_path, self.root).replace(os.sep, "/")

        if not abs_path.endswith(".md") or not os.path.isfile(abs_path):
            body = PAGE_TEMPLATE.format(
                title="未找到",
                nav=build_nav(self.root, rel_path),
                crumbs=make_crumbs(rel_path),
                content=f'<h1>404</h1><p class="empty">找不到文档：'
                f"{html.escape(rel_path)}</p>",
                relpath=html.escape(rel_path),
            )
            self._send_html(body, status=404)
            return

        with open(abs_path, "r", encoding="utf-8") as fh:
            text = fh.read()

        title = rel_path.rsplit("/", 1)[-1]
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break

        body = PAGE_TEMPLATE.format(
            title=html.escape(title),
            nav=build_nav(self.root, rel_path),
            crumbs=make_crumbs(rel_path),
            content=render_markdown(text),
            relpath=html.escape(rel_path),
        )
        self._send_html(body)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--root", default=".", help="Repository root to serve")
    args = parser.parse_args()

    DocsHandler.root = os.path.abspath(args.root)
    server = ThreadingHTTPServer((args.host, args.port), DocsHandler)
    print(
        f"[serve_docs] Serving Markdown workspace from {DocsHandler.root}\n"
        f"[serve_docs] Open http://{args.host}:{args.port}/  (Ctrl+C to stop)"
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[serve_docs] Shutting down.")
        server.shutdown()


if __name__ == "__main__":
    main()
