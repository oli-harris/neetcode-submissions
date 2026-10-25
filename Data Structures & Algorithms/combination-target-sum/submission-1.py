class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def dfs(curr, path, allowedNums):
            if curr == target:
                return combinations.append(path)
            if curr > target or len(allowedNums) == 0:
                return

            num = allowedNums[0]
            dfs(curr + num, path + [num], allowedNums)
            dfs(curr, path, allowedNums[1:])

        dfs(0, [], nums)
        return combinations
