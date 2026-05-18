class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic decreasing order: stack is in decreasing oder
        #keep adding numbers to stack, if num is greater, get index difference
        #else keep num in stack
        #place index diff in output []
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res

            
