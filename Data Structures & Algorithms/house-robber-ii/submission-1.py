class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def robber(nums):
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[:2])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

            return dp[-1]

        return max(robber(nums[1:]), robber(nums[:-1]))

    
