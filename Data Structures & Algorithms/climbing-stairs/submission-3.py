class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * n

        def dfs(i):
            if i >= n:
                return i == n
            if dp[i]:
                return dp[i]

            dp[i] = dfs(i + 1) + dfs(i + 2)

            return dp[i]


        return dfs(0)
        