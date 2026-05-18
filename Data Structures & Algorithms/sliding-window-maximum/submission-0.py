class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        vals = []
        i, j = 0, k - 1
        while (j <= len(nums) - 1):
            temp = nums[i:j+1]
            val = max(temp)
            vals.append(val)
            i+= 1
            j+= 1
        return vals