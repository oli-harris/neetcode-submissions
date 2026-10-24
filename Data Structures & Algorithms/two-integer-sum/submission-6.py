class Solution:
    # Solutions
    # - Brute Force
    # - Sort + Two pointer
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = [[num, i] for i, num in enumerate(nums)]
        A.sort()

        l, r = 0, len(nums) - 1
        while l < r:
            cur = A[l][0] + A[r][0]
            
            if cur < target:
                l += 1
            elif cur > target:
                r -= 1
            else:
                return [min(A[l][1], A[r][1]),
                        max(A[l][1], A[r][1])]


            