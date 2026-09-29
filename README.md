# Leno's Algorithm Study

用一句直觉建立整体框架，用少量因果步骤理解算法，再把思路对应到代码。

## 教学方式

- **题目概览**：一句话清晰描述题目到底在问什么。如果较为复杂，就清晰抽象。
- **题目引导**：简单列出题目给定的具体内容，break down要比题目描述更清晰直白。
- **一句直觉**：先知道我们究竟在做什么。
- **三四个要点**：建立完整的因果链。
- **局部展开**：哪里没接上，就只解释那个连接。
- **对应代码**：理解动作的意义后，再看公式和变量如何实现它。

尤其注意区分“为什么需要寻找这个候选”和“如何快速找到它”。简短不能省略关键推理。

## 笔记标准

**严格保持 notes 的直觉性（intuitivity）和简洁性。目标是读完 intuition，就有能力自己实现算法。**

- 用一句直觉和少量因果要点说明核心思维，只展开影响实现的关键连接。
- 拒绝繁杂分析、案例推断和重复解释。
- notes 写思路，solutions 放实现。凡是不帮助从直觉走到实现的内容，都不写。
- 新笔记使用两个大标题：`1. 核心直觉` 提炼原理，`2. 具体做法` 说明算法步骤与实现思路。

## 题目

| 题目 | 直觉笔记 | Python 实现 |
| --- | --- | --- |
| 2. Add Two Numbers | [notes](notes/2-add-two-numbers.md) | [solutions](solutions/2-add-two-numbers.py) |
| 210. Course Schedule II | [notes](notes/210-course-schedule-ii.md) | [solutions](solutions/210-course-schedule-ii.py) |
| 235. Lowest Common Ancestor of a Binary Search Tree | [notes](notes/235-lowest-common-ancestor-of-a-binary-search-tree.md) | [solutions](solutions/235-lowest-common-ancestor-of-a-binary-search-tree.py) |
| 1091. Shortest Path in Binary Matrix | [notes](notes/1091-shortest-path-in-binary-matrix.md) | [solutions](solutions/1091-shortest-path-in-binary-matrix.py) |
| 1392. Longest Happy Prefix | [notes](notes/1392-longest-happy-prefix.md) | [solutions](solutions/1392-longest-happy-prefix.py) |
| 1834. Single-Threaded CPU | [notes](notes/1834-single-threaded-cpu.md) | [solutions](solutions/1834-single-threaded-cpu.py) |
| 3433. Count Mentions Per User | [notes](notes/3433-count-mentions-per-user.md) | [solutions](solutions/3433-count-mentions-per-user.py) |
| 最小化最长连续相同字符段 | [notes](notes/minimize-longest-run.md) | [solutions](solutions/minimize-longest-run.py) |
| Kac Ring 1：单步模拟 | [notes](notes/kac-ring-1.md) | [solutions](solutions/kac-ring-1.py) |
| Kac Ring 2：任意步数跳转 | [notes](notes/kac-ring-2.md) | [solutions](solutions/kac-ring-2.py) |

## 在 Codex 中使用

1. 克隆仓库：

   ```sh
   git clone https://github.com/Lenoplus42/leno-s-algorithm-study.git
   ```

2. 在 Codex 中将克隆后的文件夹打开为项目。
3. 根目录 `AGENTS.md` 自动提供项目默认规则：始终用中文回答；算法及 coding style 问题必须读取教学 skill，无需额外提示词。

4. 教学 skill 位于 `.agents/skills/intuition-first-tutor/SKILL.md`，按需读取两份独立模式文件：

   - 普通模式：`references/default-mode.md`，默认启用，先直觉再逐步对应代码。
   - D mode：`references/d-mode.md`，仅显式触发时读取，以候选人身份一次完成推导、思路、完整注释代码和复杂度分析。例如：

   ```text
   D mode：实现一个 Kac ring，支持 step()、step_k(k) 和 color()。
   ```

   D mode 在当前题目的后续追问中持续生效，明确退出后恢复普通模式；新任务没有触发词时使用普通模式。仅讨论模式配置不会触发答题。

修改规则后，在本项目中新建任务验证加载情况；若规则未加载，检查工作目录及 `AGENTS.override.md` 等覆盖文件。也可以直接阅读 [SKILL.md](.agents/skills/intuition-first-tutor/SKILL.md)，将其中的教学方法用于其他助手。

## 跨电脑与共享

另一台电脑克隆同一个仓库即可获得 skill。更新后提交并推送，在另一台电脑拉取更新。Git 同步文件，不同步 Codex 对话历史。

欢迎朋友们使用、fork 和改进。直觉笔记放在 `notes/`，代码放在 `solutions/`。

## License

[MIT](LICENSE)
