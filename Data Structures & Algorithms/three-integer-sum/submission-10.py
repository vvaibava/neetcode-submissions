class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()          
        groups = set()    

        for i in range(len(nums)):
                m = i + 1
                j = len(nums) - 1
                while m < j: 
                    if nums[i] + nums[j] + nums[m] < 0: 
                        m += 1
                    elif nums[i] + nums[j] + nums[m] > 0:
                        j -= 1
                    else:
                        groups.add((nums[i], nums[j], nums[m]))
                        m += 1
                        j -= 1

        res = []
        for g in groups:
            res.append(list(g))
        
        return res

