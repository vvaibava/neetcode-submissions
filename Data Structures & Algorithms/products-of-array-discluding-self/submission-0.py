class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums: 
            i = nums.index(n)
            prod = math.prod(nums[:i]) * math.prod(nums[i + 1:])
            res.append(prod)
        
        return res
