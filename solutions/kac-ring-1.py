class KacRing:
    """固定标记、全白初始状态的环；支持单步移动和 O(1) 颜色查询。"""

    def __init__(self, n: int, marked_points: list[int]):
        if n <= 0:
            raise ValueError("n 必须大于 0")
        if any(position < 0 or position >= n for position in marked_points):
            raise ValueError("标记位置必须在 [0, n) 范围内")
        if len(set(marked_points)) != len(marked_points):
            raise ValueError("标记位置不能重复")

        self.n = n
        self.marked_points = list(marked_points)
        # 下标始终对应球的固定编号，移动时不搬动数组元素。
        self.is_white = [True] * n
        self.white_count = n
        self.offset = 0

    def step(self) -> None:
        for position in self.marked_points:
            # 球 i 位于 (i + offset) % n；减去 offset 反推编号。
            # 取模让跨过位置 0 的编号仍落在 [0, n) 内。
            ball_id = (position - self.offset) % self.n
            if self.is_white[ball_id]:
                self.white_count -= 1
            else:
                self.white_count += 1
            self.is_white[ball_id] = not self.is_white[ball_id]

        # 按出发位置翻色，全部处理完后再让所有球顺时针移动一格。
        self.offset = (self.offset + 1) % self.n

    def color(self) -> float:
        # 黑球数为 n - white_count，因此 W - B = 2W - n。
        return (2 * self.white_count - self.n) / self.n
