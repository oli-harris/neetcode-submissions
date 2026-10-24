class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        # Brute force
        for i in range(len(nums)):
            duplicate = False

            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    duplicate = True
                    break
            
            if not duplicate:
                return nums[i]
            
