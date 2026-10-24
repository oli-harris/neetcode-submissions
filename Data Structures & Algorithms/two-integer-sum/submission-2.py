class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} # stores num: index

        for i in range(len(nums)):
            if target - nums[i] in nums_map:
                return [nums_map[target - nums[i]], i]
            else:
                nums_map[nums[i]] = i