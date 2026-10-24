class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = nums[0]
    
        # First pass, inserting prefix into result
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i]
        
        # Second pass, calcuate postfix as go and insert producct
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                res[i] = postfix
            else:
                res[i] = res[i - 1] * postfix
                postfix *= nums[i]

        return res