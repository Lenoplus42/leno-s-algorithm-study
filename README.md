# Leno's Algorithm Study

用一句直觉建立整体框架，用少量因果步骤理解算法，再把思路对应到代码。

## 教学方式

- **一句直觉**：先知道我们究竟在做什么。
- **三四个要点**：建立完整的因果链。
- **局部展开**：哪里没接上，就只解释那个连接。
- **对应代码**：理解动作的意义后，再看公式和变量如何实现它。

尤其注意区分“为什么需要寻找这个候选”和“如何快速找到它”。简短不能省略关键推理。

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

欢迎朋友们使用、fork 和改进。后续题解可放在 `notes/`，代码可放在 `solutions/`。

## License

[MIT](LICENSE)
