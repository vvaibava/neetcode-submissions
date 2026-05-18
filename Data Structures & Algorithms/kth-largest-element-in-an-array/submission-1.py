class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #use nlargest(k, nums) --> outputs an array of largest nums
        #last element of that
        return heapq.nlargest(k, nums)[-1]
            

