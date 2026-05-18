class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set() 
        for i in range(len(nums)):
            if nums[i] in vals:
                return True
            vals.add(nums[i])
        return False


