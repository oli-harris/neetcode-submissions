class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort to allow for two pointer
        res = []

        for i in range(len(nums)):
            # Guard all numbers > 0 (no solution after this point)
            if nums[i] > 0:
                break

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                # move pointer toward threeSum solution
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    # found solution
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    # try find another, non duplicate solution
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res