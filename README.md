# GreenShield Plus · 产品设计工作台

这是 Evan Zhai 的私人设计仓库：用文件夹和 Markdown 文档，把产品前期研究、交互原型、设计稿、设计系统和交付物放在同一个地方。

你不需要会写代码。在 GitHub 网页上点进文件夹、复制模板、填写内容即可。大文件（Figma 源文件、视频）请放在 Figma 或共享盘，这里只放说明、链接、清单和导出的预览图。

---

## 这套体系解决什么

| 你的工作 | 对应文件夹 | 放什么 |
| --- | --- | --- |
| 前期研究与策划迭代 | [`01-research-and-planning/`](01-research-and-planning/) | 项目简介、调研计划、访谈、人物画像、机会点、迭代记录 |
| 交互原型与设计稿 | [`02-prototypes-and-designs/`](02-prototypes-and-designs/) | 信息架构、用户流程、线框、原型链接、界面稿、评审记录 |
| 设计系统 | [`03-design-system/`](03-design-system/) | 颜色/字体/间距、组件、模式、文案语气、Figma 库链接 |
| 设计交付 | [`04-delivery/`](04-delivery/) | 交接说明、标注、切图清单、走查、上线说明 |
| 参考资料 | [`05-resources/`](05-resources/) | 竞品、灵感、会议纪要、外部参考 |
| 已结束项目 | [`99-archive/`](99-archive/) | 不再活跃的项目整包归档 |

使用说明、命名规则、新建项目步骤在 [`00-guide/`](00-guide/)。

---

## 怎么开始（第一次）

1. 打开 [`00-guide/how-to-use.md`](00-guide/how-to-use.md)，用 5 分钟看完「日常三件事」。
2. 打开示例项目 `_example-claims-status`，顺着三个文件夹走一遍完整流程：
   - [研究与策划](01-research-and-planning/projects/_example-claims-status/)
   - [原型与设计稿](02-prototypes-and-designs/projects/_example-claims-status/)
   - [交付](04-delivery/projects/_example-claims-status/)
3. 按 [`00-guide/new-project-checklist.md`](00-guide/new-project-checklist.md) 复制模板，建你的第一个真实项目。

**同一个项目在三个工作区用同一个英文短名**，例如 `2026-09-claims-status`。这样以后找文件不会乱。

---

## 文件夹总览

```text
00-guide/                      怎么用这套仓库
01-research-and-planning/      研究 · 策划 · 迭代
02-prototypes-and-designs/     流程 · 线框 · 原型 · 界面稿
03-design-system/              跨项目共用的设计系统
04-delivery/                   交给工程 / 业务的交付包
05-resources/                  不绑死某个项目的资料
99-archive/                    已结束或取消的项目
```

每个文件夹里都有自己的 `README.md`，说明「这里放什么、不放什么、下一步点哪里」。

---

## 项目状态（写在各区的 `_index.md` 里）

| 状态 | 含义 |
| --- | --- |
| 构思中 | 还在定义问题 |
| 调研中 | 正在访谈、桌面研究、竞品分析 |
| 设计中 | 流程、线框、原型或视觉进行中 |
| 评审中 | 等业务 / 工程 / 合规反馈 |
| 交付中 | 已出交接包，跟开发走查 |
| 已上线 | 主流程已发布 |
| 已归档 | 不再改，整包移到 `99-archive/` |

---

## GreenShield 设计时请默认记住

- **无障碍**：健康与福利产品要按 WCAG 2.2 AA 来想对比度、焦点、表单错误。
- **中英法**：对外会员界面通常需要英 / 法；内部工具再确认语言范围。
- **隐私**：不要把真实会员姓名、保单号、理赔细节写进这个仓库。示例和笔记用虚构数据。
- **源文件在 Figma**：本仓库记录决策和链接，不存 `.fig` 大文件。

---

## 需要帮助时

- 不知道文件叫什么 → [`00-guide/naming-conventions.md`](00-guide/naming-conventions.md)
- 不知道词是什么意思 → [`00-guide/glossary.md`](00-guide/glossary.md)
- 要新建项目 → [`00-guide/new-project-checklist.md`](00-guide/new-project-checklist.md)
