# 新建项目清单

开一个新项目时，从上到下勾。第一次可以边做边对照 `_example-claims-status`。

## 开项目当天

- [ ] 想好**一句话问题**（我们要让谁、在什么情境下、做成一件什么事）。
- [ ] 起好项目短名：`YYYY-MM-short-english-name`（见[命名规则](naming-conventions.md)）。
- [ ] 在 `01-research-and-planning/projects/` 下建同名文件夹，并复制示例项目的子文件夹结构。
- [ ] 从 `_templates/01-project-brief.md` 复制出 `00-brief/project-brief.md` 并填完。
- [ ] 写该项目的 `README.md`（状态、主人、Figma 链接先空着也行）。
- [ ] 在 `01-research-and-planning/_index.md` 加一行。

## 研究启动时

- [ ] 复制 `02-research-plan.md` → `01-discovery/research-plan.md`。
- [ ] 需要访谈则复制访谈大纲和笔记模板。
- [ ] 桌面研究、政策、旧产品截图放到 `01-discovery/desk-research/`，敏感数据打码。

## 开始画流程 / 线框时

- [ ] 在 `02-prototypes-and-designs/projects/` 建**同名**文件夹。
- [ ] 填 `README.md`，把 Figma 文件链接写上。
- [ ] 先写 `01-user-flows/`，再画线框，再升高保真。
- [ ] 在 `02-prototypes-and-designs/_index.md` 加一行。

## 准备交给开发时

- [ ] 在 `04-delivery/projects/` 建**同名**文件夹。
- [ ] 用 `handoff-brief.md` 和 `handoff-checklist.md` 过一遍。
- [ ] 走查清单放到 `03-qa/`。
- [ ] 在 `04-delivery/_index.md` 加一行。

## 有可复用的组件时

- [ ] 不要只把组件埋在项目 Figma 里。
- [ ] 用 `03-design-system/components/_component-template.md` 记一条。
- [ ] 在 `03-design-system/changelog.md` 写一行：日期、加了什么、哪个项目验证过。

## 不要做的事

- 不要只建一个「杂物文件夹」把 PDF、截图、会议录音全丢进去。
- 不要三个工作区各起一个不同的项目名。
- 不要把真实会员数据贴进 Markdown。
- 不要用 `最终版` 当文件名。
