class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        pi = [0] * n

        for i in range(1, n):
            # 先尝试旧字符串中最长的那一对
            j = pi[i - 1]

            # 接不上，就换下一对更短的
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]

            # 接上了（可能是最长，或者某个更短的前后缀对）
            # 就从这里继续
            if s[i] == s[j]:
                j += 1

            pi[i] = j

        return s[:pi[-1]]
