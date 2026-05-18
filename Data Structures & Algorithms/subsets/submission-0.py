class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
          #backtracking, O(n*2^n) b/c we have 2 choices for each num in nums
          #dfs(i), index of value we make decision on
          #base case: if i >= len(nums), we append subset.copy(), and return 
          #(lefT)Decision 1(include nums): append nums[i] in subset, then recursive dfs on (i + 1)
          #(right)Decision 2(not include nums): pop element from subset, then recursive dfs on (i + 1)
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res