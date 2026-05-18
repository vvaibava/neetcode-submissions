class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if number is greater than skip over it
        # 
        output = []
        l, r = 0, 0
        while (l < len(numbers)):
            val = target - numbers[l]
            if (val in numbers):
                r = numbers.index(val)
                output.append(l+1)
                output.append(r+1)
                return output
            l+=1
        return output