from collections import deque


class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> list[int]:
        following = [[] for _ in range(numCourses)]
        remaining = [0] * numCourses

        for course, prerequisite in prerequisites:
            following[prerequisite].append(course)
            remaining[course] += 1

        ready = deque(
            course for course in range(numCourses) if remaining[course] == 0
        )
        order = []

        while ready:
            course = ready.popleft()
            order.append(course)
            for next_course in following[course]:
                remaining[next_course] -= 1
                if remaining[next_course] == 0:
                    ready.append(next_course)

        return order if len(order) == numCourses else []
