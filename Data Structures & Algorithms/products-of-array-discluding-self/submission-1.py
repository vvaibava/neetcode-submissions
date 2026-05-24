class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []
        prod = 1
        for i in range(1, len(nums) + 1):
            prefix.append(prod)
            prod *= nums[i - 1]
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1): 
            suffix.append(prod)
            prod *= nums[i]
        
        suffix = suffix[::-1]
        for i in range(len(prefix)):
            product = prefix[i] * suffix[i]
            res.append(product)
        
        return res



