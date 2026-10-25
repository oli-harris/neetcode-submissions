class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        path = []

        def dfs(curr, allowedIndex):
            nonlocal path

            if curr == target:
                return combinations.append(path.copy())
            if curr > target or allowedIndex >= len(nums):
                return

            path.append(nums[allowedIndex])
            dfs(curr + nums[allowedIndex], allowedIndex)
            path.pop()
            dfs(curr, allowedIndex + 1)

        dfs(0, 0)
        return combinations
