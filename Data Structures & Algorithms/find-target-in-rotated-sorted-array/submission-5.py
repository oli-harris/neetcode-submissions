class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            print(nums[l:r+1])
            m = l + (r - l) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[r]:
                # [l, m] sorted
                if nums[m] > target and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # [m, r] sorted
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

                    

        
        return -1
        