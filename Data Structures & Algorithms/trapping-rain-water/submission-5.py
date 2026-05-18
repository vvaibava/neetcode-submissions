class Solution:
    def trap(self, height: List[int]) -> int:
        #min(L, R) - height[l]
        #0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
        #l                                r
        if not height:
            return 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        water = 0
        while (l < r):
            curr = 0
            if height[l] < height[r]:
                l+= 1
                maxLeft = max(maxLeft, height[l])
                curr = maxLeft - height[l]

            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                curr = maxRight - height[r]

            if curr >= 0:
                water += curr
        
        return water
            

        