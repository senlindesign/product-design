[English](README.md) | [中文](README.zh-CN.md)

# Proof

![Proof — 产品设计技能](docs/images/cover.png)

### 一个产品设计技能

[![Website](https://img.shields.io/badge/Website-proofdesign.pages.dev-1F5EFF?style=flat-square)](https://proofdesign.pages.dev)
[![Made for Claude Code](https://img.shields.io/badge/Made%20for-Claude%20Code-blueviolet?style=flat-square&logo=anthropic)](https://docs.anthropic.com/en/docs/claude-code)
[![Made for Codex](https://img.shields.io/badge/Made%20for-Codex-000000?style=flat-square&logo=openai)](https://openai.com/index/introducing-codex/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![8 Page Types](https://img.shields.io/badge/8-Page%20Types-141414?style=flat-square)](#页面类型)
[![10 Sections](https://img.shields.io/badge/10-Sections-5DDFD7?style=flat-square)](#区块)
[![4 Styles](https://img.shields.io/badge/4-Styles-CF9FFC?style=flat-square)](#风格)
[![400+ Real Product Pages](https://img.shields.io/badge/400+-Real%20Product%20Pages-E9E9E9?style=flat-square)](#怎么做出来的)

**做出来的页面像真实上线的产品，不像 AI 生成的。所有做法都来自 400 多个真实产品页面。**

Proof 是一个产品设计技能，可以在 Claude Code 和 Codex 里用。告诉它你要哪个页面，它就做出一个完整的响应式页面：首屏有真实感的产品展示，有鲜明的视觉风格，动效展示的是产品在工作的样子。第一稿看上去就像一个已经上线的产品，不像 AI 模板。

**在线看效果 → [proofdesign.pages.dev](https://proofdesign.pages.dev)**：四种风格、九种页面配置、十类区块，每一个都是这个技能真实生成的页面，点开就能滚动、悬停、随手点点。

```bash
/proof landing
```


---

## 它强在哪

**1. 学自真实产品，不是模型自己的审美。**
我们通过 [Mobbin](https://mobbin.com) 的 MCP 研究了 400 多个真实上线产品的页面，把好用的做法记了下来：首屏放什么，真实网站怎么展示自己的产品，证据放哪里，区块之间布局怎么变化，真实的标题怎么写。每个做法都写了原因，也写了什么时候不该用。

**2. 四种风格，各有性格。**
Minimal、Business、Colorful、Editorial 都是完整的设计系统，每种都从一个真实产品网站里提取出来。每种风格都有自己的招牌首屏、自己的质感细节、自己的动效。同一个页面换一种风格，是两个不同的设计，不是换个颜色。

**3. 让人停下来的首屏。**
每个页面都用所选风格专属的产品展示开场：带功能标签的多色渐变舞台、飘着网点云的天空里升起一张纸质产品页、报纸头版式的深色舞台，或者精确的网格标本场。里面的产品界面填满了真实感的内容，有人名、状态、数字，绝不是灰色占位框。

**4. 整个官网都能做，一个区块也能做。**
8 种页面类型和 10 个区块，覆盖产品官网需要的主要内容。可以要一个完整的落地页，也可以只要一个价格表、一组 FAQ 或一个页脚。

**5. 接得住你的品牌和内容。**
品牌色、字体、目标用户、真实素材，有多少给多少。页面结构会按你的访客来调整。你没给的部分，会用看起来完整的示例内容填上，第一稿不会空；交付时的 QA 报告会列出每一处示例，方便你替换。

**6. 交给你之前，先自己检查。**
交付前，它会检查自己做的页面：布局节奏、风格是否到位、logo 是不是真的、有没有把编造的内容当成事实。然后告诉你哪些检查通过了。

**它会避开的东西**：AI 页面最常见的样子。

- 同一个居中模板从上重复到下
- 三张一模一样的功能卡片
- 灰色占位框和手画的 logo
- 只有蓝和紫的两色渐变
- 把编造的内容当成事实
- 所有内容都是淡入上移

---

## 风格

*同一个需求（"Relay，给客服团队用的共享收件箱"）在四种风格下的首屏（点图片可以打开在线页面）：*

| Minimal | Business |
| --- | --- |
| [![Minimal](docs/images/style-minimal.png)](https://proofdesign.pages.dev/style-minimal-relay) | [![Business](docs/images/style-business.png)](https://proofdesign.pages.dev/style-business-relay) |
| **Colorful** | **Editorial** |
| [![Colorful](docs/images/style-colorful.png)](https://proofdesign.pages.dev/style-colorful-relay) | [![Editorial](docs/images/style-editorial.png)](https://proofdesign.pages.dev/style-editorial-relay) |

| 风格 | 性格 | 招牌首屏 |
| --- | --- | --- |
| **Minimal**（默认） | 黑白灰，没有阴影，利落的直角，大量留白 | 细线网格上的"标本场"：一个主视图，周围散落真实内容的小卡片 |
| **Business** | 温暖可信，柔和阴影，圆角 | 多色渐变的圆角产品舞台，上面一排功能标签，像在带你逛产品；下面每个产品画面都垫着渐变底板 |
| **Colorful** | 有趣、有手作感，衬线标题，纸张质感的卡片 | 带颗粒和网点云的天空，一张纸质产品页从边缘升起；往下是温暖的粉彩场景 |
| **Editorial** | 有主见、沉稳，大号衬线字，一个青绿色点缀 | 报纸头版式的深色舞台：衬线大标题、一条细线，下面是一扇纸质产品窗口，旁边一栏是佐证 |

每种风格都有浅色和深色模式，也都能搭配任何页面类型。每种风格都是用 [Taste Lab](https://github.com/senlindesign/taste-skill) 从一个真实产品网站里提取的。Taste Lab 是一个测量网站风格的技能，给出具体数值（颜色、字号层级、间距、圆角、阴影），以及背后的设计原则。

---

## 为什么叫 Proof

在印刷里，proof（校样）是正式印刷前的第一份样张：已经足够接近成品，可以直接用，也是做最后调整的那一步。这个技能想做到的就是这样：第一稿就能用，你再花几分钟微调。proof 还有“证据”的意思，这个技能里的每一个做法，都来自真实上线的产品页面。

### 产品设计的五个层次

大多数设计技能只决定页面长什么样。Proof 还决定下面几层：页面放什么、按什么顺序放。因为它学的是 400 多个已经上线的产品页面，都是市场验证过的做法。分层出自 Jesse James Garrett 的《用户体验要素》。

| 层次 | 它决定什么 |
| --- | --- |
| **战略层**（推断） | 页面给谁看，要让他们做什么：从你的需求里读出来，再对照已经跑通的页面。Proof 不替你做战略。 |
| **范围层** | 放哪些区块，不放哪些区块 |
| **结构层** | 区块的先后顺序，以及布局怎么交替 |
| **框架层** | 每个区块内部怎么排 |
| **表现层** | 风格、质感和动效 |

所以同一个产品，可以得到两个不同的页面：

- **访客是想马上试用的开发者。** 你会得到一个短页面：首屏、功能、注册。
- **访客是没听说过这类产品、又担心安全的 IT 总监。** 它会加上问题说明、工作原理和安全说明。你说过还没有用户评价，所以页面上不放。

---

## 安装

### Claude Code

1. 克隆仓库：

   ```bash
   git clone https://github.com/senlindesign/proof.git
   ```

2. 把技能文件夹复制到你的技能目录：

   ```bash
   cp -R proof/skills/proof ~/.claude/skills/
   ```

3. 在任意项目里输入 `/proof`。

### Claude Code 插件

插件版可以用 `/plugin update` 更新。

1. 添加 marketplace，再安装插件：

   ```bash
   /plugin marketplace add senlindesign/proof
   /plugin install proof@proof
   ```

2. 输入 `/proof:proof`。Claude Code 会在插件技能前面加上插件名。

### skills.sh

用 [skills](https://skills.sh) 命令行一行装好，它会问你装到哪个 Agent：

```bash
npx skills add senlindesign/proof
```

装好后在 Agent 里输入 `/proof`。

### Codex

1. 克隆仓库：

   ```bash
   git clone https://github.com/senlindesign/proof.git
   ```

2. 把技能文件夹复制到 Codex 的技能目录：

   ```bash
   cp -R proof/skills/proof ~/.codex/skills/
   ```

### 其他 Agent

Cursor、Windsurf，或者其他能读文件的 Agent：让它读 `skills/proof/SKILL.md`。

这个技能不用构建，没有依赖。如果装了 Python 3，它交付前会检查每个页面。

---

## 怎么用

| 你想要 | 输入 |
| --- | --- |
| 马上要一个落地页 | `/proof landing` |
| 指定风格和深浅色的页面 | `/proof pricing editorial dark` |
| 只要一个区块 | `/proof hero colorful` |
| 贴合你产品的页面 | `/proof landing — Patchwork，给设计工作室用的共享灵感板` |
| 按你的用户来设计的页面 | 补充四件事：谁会来，要让他们做什么，他们担心什么，你有哪些真实素材。也可以直接贴 PRD 或品牌规范。 |
| 用上你的品牌 | `/proof landing business — 主色 #E4572E，标题字体 Manrope` |
| 全部自己定 | `/proof blog editorial dark — 用 archetype B，不要订阅区块，做成这个项目里的 Next.js 页面` |
| 还没想好 | 只输入 `/proof`。它会问一轮问题，然后做出页面。 |

默认输出一个 HTML 文件，用浏览器打开就能看。如果你需要，它也可以按你项目的技术栈写代码。

---

## 能做什么

![8 page types × 10 sections × 4 styles](docs/images/overview.png)

### 页面类型

每种页面类型有 3 到 4 个 archetype。archetype 是针对一类产品或目标的页面布局。

| 页面类型 | 用途 | Archetype |
| --- | --- | --- |
| **Landing** | 向新访客介绍你的产品 | SaaS Tool · SaaS Platform · Developer Tool · Creative Tool |
| **Pricing** | 套餐和收费方式 | Feature-Tiered · Usage-Based · Simple Binary · Enterprise-First |
| **Product** | 给正在评估的人细讲功能 | Feature Showcase · Platform Overview · Product Deep-Dive |
| **About** | 公司和团队的故事 | Company Story · Team-First · Mission-Driven |
| **Contact** | 咨询、支持、预约演示 | Simple Contact · Department Routing · Sales-Focused · Support Hub |
| **Blog** | 文章和更新日志列表 | Grid Index · Editorial · Minimal List |
| **Downloads** | 桌面应用、命令行工具、SDK | Platform Selector · Multi-Product · Developer Distribution |
| **404** | 帮走丢的访客找到路 | Minimal Redirect · Navigational Recovery · Brand Moment |

### 区块

`hero` · `features` · `social-proof` · `cta` · `faq` · `how-it-works` · `comparison-table` · `contact-form` · `navigation` · `footer`

### 每个页面都自带

- **真实感的产品展示**：8 种配方（叠放的卡片、从首屏底部升起的产品、界面拼成的 bento、代码窗口、AI 对话等），填满真实感的内容。
- **招牌手法**：17 种在真实网站上见过的大胆布局，比如横跨整屏的大标题、带主格的 bento、带产品画面的步骤卡、引语墙。每个页面用一到两种。
- **氛围与质感**：多色渐变、颗粒、网点、纸片拼贴，颜色都来自风格自己的色板。
- **为产品服务的动效**：数据一行行流进来，光标点一下按钮，回复自己打出来，图表画出来。都会尊重系统的"减少动态效果"设置。
- **只用真实 logo**：集成、客户、平台的 logo 都来自图标库，不让 AI 自己画。
- **真实的文案写法**：标题按 72 条真实标题总结出的写法来写，短、具体、句首大写。

---

## 怎么做出来的

- **研究真实产品。** 通过 [Mobbin](https://mobbin.com) 的 MCP，我们为真实产品页面写了 410 份详细记录（每种页面类型 28 到 63 份），之后又研究了 55 个产品展示、32 个招牌手法和 72 条标题。
- **设计模式都带着原因。** 每个模式都写清楚什么时候适用、怎么做、什么时候该跳过。常见的模式，不一定是对的模式。
- **有第二个 agent 专门挑错。** 另一个 agent 拿研究记录逐份核对知识文件，在问题进入技能之前就把矛盾修掉。
- **风格来自真实网站。** Taste Lab 在真实产品网站上测量每种风格。先有数值，再有解释这些数值的原则。
- **一套黄金测试集。** 19 个固定需求合起来覆盖全部 8 种页面类型、4 种风格和深浅两种模式。每个结果都由脚本检查，包括在 390px 窄屏下再查一遍；另一个模型核查有没有编造的内容；还有一个截图评审，给页面像不像真产品打分。详见 [`evals/`](evals/)。
- **盲测对比。** 每个新版本都会和旧版本做盲测，从真实感、产品展示、布局变化、文案四个方面打分。

---

## 仓库结构

```txt
skills/proof/              技能本体，安装的就是这个文件夹
├── SKILL.md               入口
├── pages/                 8 种页面类型，各带一组知识文件
├── sections/              10 个区块
├── scripts/               页面自检脚本
└── shared/                4 种风格、产品展示、招牌手法、氛围质感、文案、动效

evals/                     黄金测试集、页面检查、声明核查、截图评审、盲测
```

## 许可

[MIT](LICENSE)
