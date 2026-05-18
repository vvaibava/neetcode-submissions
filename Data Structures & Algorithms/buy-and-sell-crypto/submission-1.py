class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # lowest = prices[0]
        # for price in prices:
        #     if price < lowest:
        #         lowest = price
        #     res = max(res, price - lowest)
        # return res
        l, r = 0, 1
        maxP = 0
        while (r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
            r+= 1
        return maxP
