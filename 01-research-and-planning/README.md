# 01 · 研究与策划迭代

产品还没画高保真之前，以及画了之后要改方向时，都在这里工作。

## 这里放什么

- 项目为什么存在（Brief）
- 调研怎么做、做成了什么
- 人物画像、体验地图、机会点
- 策略结论，以及之后每一次改策略的记录

## 不要放什么

- 线框、原型链接、界面截图 → 去 `02-prototypes-and-designs/`
- 交给开发的标注和切图 → 去 `04-delivery/`
- 已经定下来、跨项目复用的组件规则 → 去 `03-design-system/`

## 一个项目的标准结构

```text
projects/YYYY-MM-short-name/
  README.md                 项目封面
  00-brief/                 一句话问题、范围、成功标准
  01-discovery/             计划、访谈、桌面研究
    interviews/
    desk-research/
  02-insights/              结论，不是原始笔记堆砌
    personas/
    journey-maps/
  03-strategy/              做 / 不做、优先级、指标
  04-iterations/            策划怎么改过
```

新建时复制 `_templates/`，或直接复制 `_example-claims-status` 再清空示例正文。

当前项目列表：[`_index.md`](_index.md)。
