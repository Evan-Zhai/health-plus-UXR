# 命名规则

规则少而严，是为了三个月后还能搜到文件。

## 文件夹与项目短名

格式：

```text
YYYY-MM-short-english-name
```

例子：

- `2026-09-claims-status`
- `2026-10-provider-search`
- `2026-11-member-onboarding`

要求：

- 只用小写英文、数字和连字符 `-`
- 不要空格、不要中文文件夹名（GitHub 和工程协作更稳）
- 同一个项目在 `01` / `02` / `04` 三个区必须同名
- 示例项目以 `_example-` 开头，模板说明以 `_` 开头，避免和真项目混在一起

## 文件名

格式：

```text
topic-or-artifact.md
```

例子：

- `project-brief.md`
- `research-plan.md`
- `persona-busy-parent.md`
- `flow-submit-claim.md`
- `handoff-checklist.md`

要求：

- 全小写 + 连字符
- 一种文档一种名字，不要 `brief-v3-final.md`
- 版本用 Git 历史，不靠文件名堆 `v2`
- 被替代的旧文件：在文首写「已被 `新文件名` 替代」，或把文件名改为 `topic.superseded.md`

## 设计稿与导出图

仓库里的预览图：

```text
screen-<flow>-<step>.png
```

例如：`screen-submit-claim-review.png`

Figma 页面 / Frame 建议同步：

```text
[Flow] Submit claim / 03 Review
```

## 设计系统

- 基础：`foundations/<topic>.md` → `color.md`
- 组件：`components/<name>.md` → `button.md`
- 模式：`patterns/<name>.md` → `form-validation.md`

组件名用产品里说的英文名，和 Figma 组件名保持一致。

## 日期

正文里的日期一律 `YYYY-MM-DD`，例如 `2026-09-03`。
