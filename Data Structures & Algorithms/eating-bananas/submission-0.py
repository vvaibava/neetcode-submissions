class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #h must be less than or equal to size of pile b/c 1 pile/hr
        #initialize l, r and loop through for k, and increment hours
        #if hours is less than h, we update the rate, and move r 
        #else, update rate, and move l
        l, r = 1, max(piles)
        rate = r
        while (l <= r): 
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                rate = min(rate, k)
                r = k - 1
            else: 
                l = k + 1
        return rate
                
