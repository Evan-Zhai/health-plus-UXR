# 日常怎么用这个仓库

你只需要会三件事：**按层级找地方、复制项目工具包、填写并保存**。

## 找地方（五层）

| 层级 | 问自己 | 例子 |
| --- | --- | --- |
| 1 业务板块 | 这是 Plus 产品、设计系统，还是跨产品通用？ | `01-greenshield-plus/` |
| 2 功能模块 | 落在 core、药房、问诊还是咨询？ | `core/` |
| 3 页面 / 功能 | 具体是哪一页或哪块能力？ | `personalization/` |
| 4 项目 | 这一页上的哪一轮迭代？ | `projects/2026-09-welcome-cards/` |
| 5 工作职责 | 这是研究、设计稿，还是测试？ | `user-research/` |

同一页面会有很多轮项目，**不要覆盖旧项目文件夹**。新开一轮就新建一个 `YYYY-MM-短名`。

还没有拆到页面的模块（pharmacy / telemed / counselling）：先把项目放在该模块 README 里登记，页面名字确定后再建与 `personalization` 同级的文件夹，把项目挪进去。

## 复制模板

完整空项目在 [`../_templates/project-kit/`](../_templates/project-kit/)。做法：

1. 对照工具包，在目标页面的 `projects/` 下建同名结构（或请 Cursor 按工具包复制一份并改名）。
2. 打开模板，把 `{{ }}` 换成真实内容。
3. 用不到的章节删掉，不要硬填。
4. 在该页面的 `_index.md` 加一行。

对照示例：[`../01-greenshield-plus/core/personalization/projects/_example-welcome-cards/`](../01-greenshield-plus/core/personalization/projects/_example-welcome-cards/)。

## 填写并保存

在 GitHub 网页上：打开文件 → 铅笔图标 → 修改 → 底部写一句说明 → Commit。

历史靠 Git 记住，不要用「最终版-真的最终版」当文件名。

## 什么放这里，什么不放

| 放进 GitHub | 不要放进 GitHub |
| --- | --- |
| Markdown 说明、清单、决策 | 真实会员 / 理赔 / 健康数据 |
| Figma、原型的链接 | `.fig` / 长视频 |
| 导出的小预览图 | 密码、未公开合同原文 |

## 和 Figma 怎么分工

| 问题 | 写在仓库 | 做在 Figma |
| --- | --- | --- |
| 这轮项目解决什么、范围多大 | `research-and-planning/design-scope/` | — |
| 竞品、数据、用户研究 | 对应研究子文件夹 | FigJam 可选 |
| 页面长什么样、能不能点 | `prototypes-and-designs/` 清单 + 链接 | 线框 / 高保真 / 原型 |
| 测了什么、改了什么 | `user-testing/` | 测试用原型 |
| 组件用哪一种 | `02-design-system/` + Figma 库链接 | 组件库（当前和开发沟通的主渠道） |

## 一轮项目结束时

1. 把该页面 `_index.md` 里这一行改成「已上线」或「已归档」。
2. **文件夹留在该页面的 `projects/` 里**，方便以后同页新项目对照。
3. 若有可复用的组件或规则，记到 `02-design-system/`，不要只埋在项目 Figma 里。
