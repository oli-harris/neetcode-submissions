

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = right

        while left <= right:
            mid = (left + right) // 2

            hours = sum([math.ceil(pile / mid) for pile in piles])
            
            if hours > h:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return res