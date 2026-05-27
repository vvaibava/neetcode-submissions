class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = set(nums)

        count = 0
        for n in sortedNums: 
            if (n - 1) not in sortedNums: 
                val = n
                curr = 0
                while val in sortedNums:
                    curr += 1
                    val += 1
                count = max(count, curr)
            else:
                continue
        
        return count

