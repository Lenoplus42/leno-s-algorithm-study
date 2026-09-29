class KacRing:
    """预计算一个周期，支持 O(1) 单步、跳步和颜色查询。"""

    def __init__(self, n: int, marked_points: list[int]):
        if n <= 0:
            raise ValueError("n 必须大于 0")
        if any(position < 0 or position >= n for position in marked_points):
            raise ValueError("标记位置必须在 [0, n) 范围内")
        if len(set(marked_points)) != len(marked_points):
            raise ValueError("标记位置不能重复")

        self.n = n
        self.phase = 0
        # 一圈翻色 M 次：M 偶数时一圈恢复，奇数时两圈恢复。
        self.period = n if len(marked_points) % 2 == 0 else 2 * n
        self.white_counts = []
        is_white = [True] * n
        white_count = n

        for offset in range(n):
            # 先记录第 offset 步，再模拟下一步；表中先保存第 0 到 n-1 步。
            self.white_counts.append(white_count)
            for position in marked_points:
                # 当前位置 = 球编号 + offset；相减并取模反推球编号。
                ball_id = (position - offset) % n
                if is_white[ball_id]:
                    white_count -= 1
                else:
                    white_count += 1
                is_white[ball_id] = not is_white[ball_id]

        if len(marked_points) % 2 == 1:
            second_half = []
            for count in self.white_counts:
                # 相隔 n 步所有球颜色相反：第 t+n 步的白球数为 n-W(t)。
                second_half.append(n - count)
            # 前半段算好后，补上第 n 到 2n-1 步，得到完整周期。
            self.white_counts.extend(second_half)

    def step(self) -> None:
        self.step_k(1)

    def step_k(self, k: int) -> None:
        if k < 0:
            raise ValueError("k 必须非负")
        # 完整周期不改变状态；phase 保存累计步数在周期内的位置。
        self.phase = (self.phase + k) % self.period

    def color(self) -> float:
        white_count = self.white_counts[self.phase]
        return (2 * white_count - self.n) / self.n
