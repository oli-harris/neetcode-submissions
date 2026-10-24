class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        best = [None] * N

        for i in range(N):
            if i == 0:
                best[i] = nums[i]
                continue
            if i == 1:
                best[i] = max(nums[i], nums[i - 1])
                continue

            best[i] = max(nums[i] + best[i - 2], best[i - 1])

        return best[-1]

            