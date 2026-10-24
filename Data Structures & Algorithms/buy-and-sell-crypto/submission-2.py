class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy day
        r = 1 # sell day
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                # profit achieveable
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r # move l to r, as cheaper buy price found
            
            r += 1

        return maxP