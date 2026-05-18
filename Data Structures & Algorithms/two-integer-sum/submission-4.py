class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {} 
        for i in range(len(nums)):
            count[nums[i]] = i
        
        diff = {}
        for c in count: 
            num = target - c
            if num in nums: 
                diff[num] = nums.index(num)
        
        for c in count: 
            num = target - c
            if num in diff and count[c] != diff[num]: 
                if count[c] < diff[num]:
                    return [count[c], diff[num]]
                else:
                    return [diff[num], count[c]]
    

        
        
