class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: 
            return False

        pars = {"[":"]", "{":"}", "(":")"}
        stack = []
        for i in range(len(s)): 
            if s[i] not in pars: 
                if stack and s[i] == pars[stack[-1]]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(s[i])
        
        if not stack: 
            return True
        else:
            return False