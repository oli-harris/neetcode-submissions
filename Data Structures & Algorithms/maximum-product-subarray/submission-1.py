class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currentMin, currentMax = 1, 1

        for num in nums:
            newMax = max(num, currentMax * num, currentMin * num)
            newMin = min(num, currentMax * num, currentMin * num)

            res = max(res, newMax)
            currentMin, currentMax = newMin, newMax
        
        return res
