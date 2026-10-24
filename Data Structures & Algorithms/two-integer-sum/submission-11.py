class Solution:
    # Solutions
    # - Brute Force
    # - Sort + Two pointer
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First pass, create map of {number: index}
        positionMap = {} 
        for i, n in enumerate(nums):
            positionMap[n] = i

        # Second pass, uses map to see if possible to make target
        for i, n in enumerate(nums):
            diff = target - n
            if diff in positionMap and positionMap[diff] != i:
                return [i, positionMap[diff]]

        return []

            