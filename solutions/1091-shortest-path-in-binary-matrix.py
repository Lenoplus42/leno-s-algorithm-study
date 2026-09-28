from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        seen = {(0, 0)}

        while queue:
            r, c, distance = queue.popleft()
            if r == n - 1 and c == n - 1:
                return distance

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and grid[nr][nc] == 0
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        queue.append((nr, nc, distance + 1))

        return -1
