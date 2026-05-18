class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #difference is in this array there are duplicate values
        #Base case: if total is 0, append subset and return
        #BaseCase:  if total is < 0 or i == len(candidates) return
        #skip dups by using while loop
        res = [] 
        candidates.sort()
        subset = []
        def dfs(i, total):
            if total == 0:
                res.append(subset.copy())
                return
            if total < 0 or i == len(candidates):
                return 
            subset.append(candidates[i])
            dfs(i + 1, total - candidates[i])
            subset.pop()
            while (i + 1 < len(candidates) and candidates[i] == candidates[i + 1]):
                i += 1
            dfs(i + 1, total)
        dfs(0, target)
        return res