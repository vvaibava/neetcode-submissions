class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initiate left and right pointer
        #middle pointer is the middle of both left and right
        #if target is greater than mid, shift left to mid + 1
        #if taregt is less than mid, shift right to mid - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)// 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1 
            
