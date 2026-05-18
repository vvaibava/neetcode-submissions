class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #in order to avoid duplicates, during the decision between [2,3,6,7], if we touch 2, we dont include it again
        #recursive dfs(i, total)
        #if total is 0, add the subset to res, or if total is less or i >= len(nums) we overshot so return
        #dfs(i, total - nums[i]), then pop from subset so we dont have dups
        #dfs(i + 1, total)
        res = []
        subset = []

        def dfs(i, total):
            if total == 0:  
                res.append(subset.copy())
                return
            if total < 0 or i >= len(nums): 
                return
            
            subset.append(nums[i])
            dfs(i, total - nums[i]) 
            subset.pop()  

            dfs(i + 1, total)

        dfs(0, target)
        return res