class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        nums_set = set()

        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                nums_set.add(num)
        
        return list(nums_set)[0]
            
