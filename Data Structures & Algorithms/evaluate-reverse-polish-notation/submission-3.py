class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #if number is not an operator, add it to stack
        #if it is an operator, append the value after operator to stack
        stack = []
        for num in tokens:
            if num == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif num == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            elif num == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif num == "/":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2/val1))
            else:
                stack.append(int(num))
        return stack[0]
