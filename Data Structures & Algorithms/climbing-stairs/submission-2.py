class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None for _ in range(n)]

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0

            if dp[i]:
                res = dp[i]
            else:
                res = dfs(i + 1) + dfs(i + 2)
                dp[i] = res

            return res


        return dfs(0)
        