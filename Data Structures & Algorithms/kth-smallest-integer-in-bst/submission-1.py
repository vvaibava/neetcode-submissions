# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #iterative dfs implementation: in order traversal
        #initialize n and curr = root
        #use a stack and while curr is not null and stack is not empty, loop thru
        #go as far down left branch while appending to stack
        #if we reach a null val, then curr = stack.pop()
        #if n == k, return val
        #othewise cur = curr.right
        n = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
        