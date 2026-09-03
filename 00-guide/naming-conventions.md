# 命名规则

## 业务板块 / 模块 / 页面

只用小写英文、数字和连字符。不要空格、不要中文文件夹名。

| 层级 | 现有名字（不要擅自改） |
| --- | --- |
| 板块 | `01-greenshield-plus` · `02-design-system` · `03-universal` |
| Plus 模块 | `core` · `pharmacy` · `telemed` · `counselling` |
| Core 页面 | `personalization` · `registration` · `claim` · `coverage` |

以后新增页面：短、稳定、和产品口头说的英文一致，例如 `prescription-refill`。

## 项目文件夹

```text
YYYY-MM-short-english-name
```

例子：`2026-09-welcome-cards`、`2026-11-claim-status`。

- 示例以 `_example-` 开头，模板以 `_` 开头。
- 一轮迭代一个文件夹。同一页面的下一轮再新建，不要改名复用旧夹。
- 版本靠 Git 历史，不要 `v2-final`。

## 项目内部（工作职责）

名字固定，便于每个项目长得一样：

```text
research-and-planning/
  competitor-research/
  data-analysis/
  design-scope/
  user-research/
prototypes-and-designs/
user-testing/
```

设计系统板块工作类型还没定：先用 `02-design-system/projects/YYYY-MM-name/`，里面需要什么职责再加，不必强行套上面三套。

## 文件名

```text
topic-or-artifact.md
```

例如：`design-scope.md`、`interview-notes-p1.md`、`test-findings.md`。

正文日期一律 `YYYY-MM-DD`。被替代的旧文件在文首写「已被 `新文件` 替代」。
