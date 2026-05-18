class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0
        while(l < r):
            index = r - l
            min_val = min(heights[l], heights[r])
            product = min_val * index
            area = max(product, area)
            if(heights[l] < heights[r]):
                l+=1
            else: 
                r-=1
        return area

