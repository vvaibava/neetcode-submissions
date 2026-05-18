class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add close parenthesis if close < open
        #if open == closed == n, we have a pair
        stack = []
        res = []
        
        def backtrack(openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack))
                return

            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closedP)
                stack.pop()
            if closedP < openP:
                stack.append(")")
                backtrack(openP, closedP + 1)
                stack.pop()
        
        backtrack(0,0)
        return res