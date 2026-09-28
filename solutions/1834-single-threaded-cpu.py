import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        pending = sorted(
            (arrival, duration, index)
            for index, (arrival, duration) in enumerate(tasks)
        )
        ready = []  # (耗时, 原编号)
        order = []
        t = 0
        i = 0
        n = len(pending)

        while i < n or ready:
            if not ready:
                t = max(t, pending[i][0])

            # 收齐所有已到达任务后再选择。
            while i < n and pending[i][0] <= t:
                arrival, duration, index = pending[i]
                heapq.heappush(ready, (duration, index))
                i += 1

            duration, index = heapq.heappop(ready)
            order.append(index)
            t += duration

        return order
