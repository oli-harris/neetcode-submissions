class Solution:
    # Solutions
    # - Brute Force
    # - Sort + Two pointer
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First pass, create map of {number: index}
        prevMap = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return []

            