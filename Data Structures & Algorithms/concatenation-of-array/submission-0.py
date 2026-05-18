class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        vals = []
        for i in range(len(nums)): 
            vals.append(nums[i])
        tot = vals + nums
        return tot