[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

# 1. 核心直觉

**每算完一位，留给下一位的信息只有“进位”。** 链表从个位开始，恰好符合竖式加法的顺序，可以边遍历、边计算、边生成结果。

# 2. 具体做法

这是模拟竖式加法：

1. 两个指针指向当前待相加的位；某条链表用完，就把它的数字当作 `0`。
2. 计算 `total = x + y + carry`，把 `total % 10` 接到结果末尾，用 `total // 10` 更新进位。
3. 两个指针向后移动，重复计算，直到两条链表都用完且没有进位。

实现时，`dummy` 固定结果入口，`tail` 指向结果末尾；每次用 `tail.next` 接上新节点，再移动 `tail`。最后返回 `dummy.next`。

时间复杂度 **O(max(m, n))**，额外空间 **O(1)**（不计返回链表）。

[Python 实现](../solutions/2-add-two-numbers.py)
