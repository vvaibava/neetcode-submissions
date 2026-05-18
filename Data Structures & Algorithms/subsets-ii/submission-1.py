class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #sort input array
        #backtracking(i, subset) index of nums array and current subset
        #base case: if i equals input array nums, append subset to res
        #Case 1: all subsets that include nums[i]
        #Case 2: all subsets that don't include nums[i]
        #^^as long as i + 1 < len(nums) and nums[i] == nums[i + 1]

        res = []
        nums.sort()
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res
