class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            curr = 0
            if len(prices) == 1: 
                return curr
            i, j = 0, 1
            while j < len(prices): 
                if prices[i] < prices[j]: 
                    curr = max(curr, prices[j] - prices[i])
                elif prices[j] < prices[i]:
                    i = j
                j += 1

            return curr 