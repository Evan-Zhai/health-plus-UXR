# 新建项目清单

在**某个已有页面**上开一轮新迭代时，从上到下勾。对照 [`../01-greenshield-plus/core/personalization/projects/_example-welcome-cards/`](../01-greenshield-plus/core/personalization/projects/_example-welcome-cards/)。

## 开项目当天

- [ ] 确认落在哪个板块 / 模块 / 页面（不是先建一个「杂物夹」）。
- [ ] 若页面文件夹还不存在：在模块下新建页面夹，并加上 `README.md`、`_index.md`、`projects/`。
- [ ] 想好一句话问题。
- [ ] 起短名：`YYYY-MM-short-english-name`。
- [ ] 把 [`../_templates/project-kit/`](../_templates/project-kit/) 复制成 `…/<页面>/projects/<短名>/`。
- [ ] 填写项目 `README.md` 和 `research-and-planning/design-scope/design-scope.md`。
- [ ] 在该页面 `_index.md` 加一行。

## 研究阶段

按实际用到的子类填写，不需要的夹子留着 README 即可：

- [ ] `competitor-research/`
- [ ] `data-analysis/`（只写结论和打码后的图表说明，不贴可识别数据）
- [ ] `user-research/`

## 开始画流程 / 稿

- [ ] 产出放进**同一个项目**的 `prototypes-and-designs/`（不要另起一个项目名）。
- [ ] 项目 README 补上 Figma 链接。

## 要测试时

- [ ] 计划、场次笔记、结论放进同一项目的 `user-testing/`。
- [ ] 测试导致的策划变化，回写 `design-scope` 或在 scope 文末加迭代记录，不要默默改掉旧结论。

## 碰到设计系统缺口时

- [ ] 在 `02-design-system/gaps-and-backlog/` 记一条。
- [ ] 若本轮要补语气 / 自适应 / 网页-移动转换，到对应文件夹写草案，并在 `02-design-system/projects/` 开一个系统侧项目（可和产品项目互相链接）。

## 不要做的事

- 不要按「研究一个总夹、设计一个总夹」把同一项目拆到仓库顶层。
- 不要把真实会员数据贴进 Markdown。
- 不要用「最终版」当文件名。
- 不要把 Plus 页面的稿存进 `02-design-system/`（系统只收可复用规则）。
