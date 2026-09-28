[3433. Count Mentions Per User](https://leetcode.com/problems/count-mentions-per-user/)

给定用户和消息、离线事件，统计每个用户被提及的次数。所有用户最初在线；离线持续 60 个时间单位；同时间先处理状态变化，再处理消息。

# 1. 核心直觉

**按时间回放事件，只记每个人何时恢复在线，就能判断消息发生时谁在线。**

离线发生在 `t`，就记 `online_at[user] = t + 60`。之后用 `当前时间 >= online_at[user]` 判断在线，不需要另存在线标志、逐秒计时或生成恢复事件。

# 2. 具体做法

1. 按 `(int(timestamp), kind == "MESSAGE")` 排序：元组先比较时间，时间相同时 `False < True`，因此离线事件先处理。`key` 只提供比较依据，排序结果仍是原事件。
2. 用 `mentions` 记录次数，`online_at` 记录恢复时间，初值均为零。离线事件将对应恢复时间更新为 `t + 60`。
3. 消息为 `ALL` 时所有人加一；为 `HERE` 时，只有满足 `t >= online_at[user]` 的人加一。
4. 显式 ID 用空格拆开，去掉 `id` 前缀后逐个计数：离线也算，重复出现也算，不能去重。

原题保证离线事件引用的用户当时在线。恰好到恢复时间就已经在线，所以比较必须包含等号。

设事件数为 `E`、用户数为 `U`、显式 ID 出现总次数为 `M`。时间 **O(E log E + EU + M)**；额外空间 **O(E + U + L)**，其中 `L` 为单条消息拆分后的最大 ID 数，包含排序副本和临时拆分列表。

[Python 实现](../solutions/3433-count-mentions-per-user.py)
