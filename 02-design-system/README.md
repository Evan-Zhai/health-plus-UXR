# Design system

跨 Plus / 其他产品复用的规则与组件。**它是一个业务板块**，不是某个页面项目的子文件夹。

## 现在怎么跟开发沟通

几乎全靠 **Figma 文件和链接**（库、页面、标注）。仓库这边先把链接、缺口和以后要补的规则写清楚，不取代 Figma。详见 [`working-with-engineering/`](working-with-engineering/)。

## 已经立好的夹子

| 文件夹 | 用途 | 现在的状态 |
| --- | --- | --- |
| [`working-with-engineering/`](working-with-engineering/) | 和开发怎么同步、Figma 链接登记 | 先填链接 |
| [`foundations/`](foundations/) | 颜色、字体、间距、图标、无障碍 | 官方值待填 |
| [`components/`](components/) | 单个组件说明；很多项仍不完善 | 有模板 + 缺口表 |
| [`content-and-voice/`](content-and-voice/) | 语气规则 | **缺失，仅有草案提纲** |
| [`layout-and-responsive/adaptive-rules/`](layout-and-responsive/adaptive-rules/) | 自适应规则 | **缺失** |
| [`layout-and-responsive/web-and-mobile/`](layout-and-responsive/web-and-mobile/) | 网页端 ↔ 移动端如何转换 | **缺失** |
| [`patterns/`](patterns/) | 多组件固定用法 | 待补 |
| [`tokens/`](tokens/) | 和开发对的名字 | 草案 |
| [`gaps-and-backlog/`](gaps-and-backlog/) | 不完善组件、缺内容的总账 | 先从已知三项记起 |
| [`projects/`](projects/) | 系统侧自己的改进项目（工作类型待你定） | 空 |

工作类型还没想清楚：不要硬套 Plus 页面那三套职责。有具体改进任务时，在 `projects/YYYY-MM-name/` 下按你当时需要的产出建子夹，并在项目 README 写清「这轮补的是语气 / 组件 / 布局中的哪一块」。
