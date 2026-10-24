class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, len(prices) - 1
        maxProfit = 0

        while left < right:
            if prices[right] - prices[left] > maxProfit:
                maxProfit = prices[right] - prices[left]

            right -= 1

            if right == left:
                left += 1
                right = len(prices) - 1

        return maxProfit