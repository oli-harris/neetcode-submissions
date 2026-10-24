class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 1e9

        dp = [INF] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])



        print(dp)
        minCoins = dp[-1]
        return -1 if minCoins >= INF else minCoins
