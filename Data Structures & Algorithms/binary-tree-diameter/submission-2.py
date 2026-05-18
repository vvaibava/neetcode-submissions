# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #create a global variable to max diameter
        #recursively run through left and right
        #keep track of the variable by finding the max diameter 
        #for that node, return the height
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            a = max(left, right)
            val = 1 + max(left, right)
            return val
        dfs(root)
        return self.res