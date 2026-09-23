# Leno's Algorithm Study

用一句直觉建立整体框架，用少量因果步骤理解算法，再把思路对应到代码。

## 教学方式

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
| 1392. Longest Happy Prefix | [notes](notes/1392-longest-happy-prefix.md) | [solutions](solutions/1392-longest-happy-prefix.py) |
| 最小化最长连续相同字符段 | [notes](notes/minimize-longest-run.md) | [solutions](solutions/minimize-longest-run.py) |

## 在 Codex 中使用

1. 克隆仓库：

   ```sh
   git clone https://github.com/Lenoplus42/leno-s-algorithm-study.git
   ```

2. 在 Codex 中将克隆后的文件夹打开为项目。
3. skill 位于 `.agents/skills/intuition-first-tutor/SKILL.md`。在对话中输入：

   ```text
   $intuition-first-tutor 带我理解这道算法题。先用一句直觉和三四个极简要点讲核心思维。
   ```

如果没有发现 skill，重启 Codex 后重新打开项目。也可以直接阅读 [SKILL.md](.agents/skills/intuition-first-tutor/SKILL.md)，将其中的教学方法用于其他助手。

## 跨电脑与共享

另一台电脑克隆同一个仓库即可获得 skill。更新后提交并推送，在另一台电脑拉取更新。Git 同步文件，不同步 Codex 对话历史。

欢迎朋友们使用、fork 和改进。直觉笔记放在 `notes/`，代码放在 `solutions/`。

## License

[MIT](LICENSE)
