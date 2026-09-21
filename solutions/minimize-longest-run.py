def min_longest_run(s: str, k: int) -> int:
    """最多翻转 k 次，最小化最长连续相同字符段；k >= 0，s 仅含 a、b。"""
    n = len(s)
    if n == 0:
        return 0

    # 上限为 1 时，只能变成 abab... 或 baba...
    diff = 0
    for i in range(n):
        if i % 2 == 0:
            expected = "a"
        else:
            expected = "b"
        if s[i] != expected:
            diff += 1

    if min(diff, n - diff) <= k:
        return 1

    # 记录每段连续相同字符的长度
    runs = []
    length = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            length += 1
        else:
            runs.append(length)
            length = 1
    runs.append(length)

    # 答案 1 已排除，寻找第一个可行的上限
    left, right = 2, max(runs)
    while left < right:
        limit = (left + right) // 2
        needed = sum(length // (limit + 1) for length in runs)

        if needed <= k:
            right = limit  # 次数够用，继续尝试更小的上限
        else:
            left = limit + 1  # 次数不够，必须放宽上限

    return left
