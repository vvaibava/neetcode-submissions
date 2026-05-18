class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #keep calling recursive function w input nums w/o first element
        #go through every possible permutation and every possible index we can insert into
        #that current value(double for loop) 
        #base case: if len(nums) == 0, return [[]] --> we do a bottom top approach
        #
        if len(nums) == 0: 
            return [[]]
        perms = self.permute(nums[1:])
        res = []
        for p in perms: 
            for i in range(len(p) + 1):
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                res.append(pcopy)
        return res