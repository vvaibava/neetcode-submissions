class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums or len(nums) == 1: 
            return False

        s = set() 
        for n in nums: 
            s.add(n) 
        
        if len(nums) != len(s): 
            return True
    
        return False