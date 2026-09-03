# GreenShield Plus · 产品设计工作台

Evan Zhai 的私人设计仓库。按 **业务板块 → 功能模块 → 页面 → 项目 → 工作职责** 存放产出，方便长期迭代时既分得清产品和平台，也分得清模块和页面。

不需要会写代码。在 GitHub 网页里点文件夹、复制模板、填写即可。Figma 源文件继续放在 Figma；这里放决策、链接、清单和少量预览图。

---

## 三个业务板块

| 板块 | 文件夹 | 放什么 |
| --- | --- | --- |
| GreenShield Plus | [`01-greenshield-plus/`](01-greenshield-plus/) | 会员产品：core / pharmacy / telemed / counselling |
| Design system | [`02-design-system/`](02-design-system/) | 跨产品的系统本身；现在主要靠 Figma 文件和链接跟开发沟通 |
| Universal | [`03-universal/`](03-universal/) | 不属于单一产品线的共通工作 |

使用说明：[`00-guide/`](00-guide/)。新项目先复制 [`_templates/project-kit/`](_templates/project-kit/)。

---

## 怎么往下分（以 Plus 为例）

```text
01-greenshield-plus/                 业务板块
  core/                              功能模块
    personalization/                 页面 / 具体功能
      projects/
        2026-09-welcome-cards/       这一页上的某一个项目（长期会有多个）
          research-and-planning/     本项目的研究与策划
            competitor-research/
            data-analysis/
            design-scope/
            user-research/
          prototypes-and-designs/    本项目的原型与设计稿
          user-testing/              本项目的可用性测试
    registration/
    claim/
    coverage/
  pharmacy/                          页面尚未拆分，确定后按 core 同级加文件夹
  telemed/
  counselling/
```

**找文件的顺序**：先问「哪个产品？」→「哪个模块？」→「哪个页面？」→「哪一次项目？」→「这是研究、设计稿，还是测试？」

---

## 第一次怎么用

1. 读 [`00-guide/how-to-use.md`](00-guide/how-to-use.md)（大约 5 分钟）。
2. 打开示例项目，看一个页面里的一次迭代长什么样：  
   [`01-greenshield-plus/core/personalization/projects/_example-welcome-cards/`](01-greenshield-plus/core/personalization/projects/_example-welcome-cards/)
3. 按 [`00-guide/new-project-checklist.md`](00-guide/new-project-checklist.md) 在对应页面的 `projects/` 下建你的第一个真实项目。

---

## 设计系统现在缺什么

沟通现状写在 [`02-design-system/working-with-engineering/`](02-design-system/working-with-engineering/)。已经单独建好、但内容仍待补的缺口：

- 语气规则 → [`02-design-system/content-and-voice/`](02-design-system/content-and-voice/)
- 自适应规则 → [`02-design-system/layout-and-responsive/adaptive-rules/`](02-design-system/layout-and-responsive/adaptive-rules/)
- 网页端 ↔ 移动端布局如何转换 → [`02-design-system/layout-and-responsive/web-and-mobile/`](02-design-system/layout-and-responsive/web-and-mobile/)

工作类型还没定死：先把夹子立住，以后在 [`02-design-system/projects/`](02-design-system/projects/) 里按项目往里填。

---

## 项目状态

写在该**页面**的 `_index.md` 里，不要拆到三个地方各记一笔。

| 状态 | 含义 |
| --- | --- |
| 构思中 | 还在定义问题 |
| 调研中 | 竞品、数据、用户研究进行中 |
| 设计中 | 流程、线框、原型或视觉进行中 |
| 测试中 | 可用性测试或走查 |
| 评审中 | 等业务 / 工程 / 合规 |
| 已上线 | 这一轮已发布 |
| 已归档 | 不再改；文件夹留在该页面的 `projects/` 里当历史 |

---

## 默认记住

- 对外会员产品按 WCAG 2.2 AA 想对比度、焦点、表单错误。
- 对外界面通常要英 / 法。
- 不要把真实会员姓名、保单号、理赔或健康细节写进仓库。
- `.fig` 大文件不进 Git，只写链接。
