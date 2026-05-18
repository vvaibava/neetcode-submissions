# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #initialize left and right pointer
        #check if root is None]
        #recursively go down and increment then choose the max
        l, r = 0, 0 
        if not root:
            return 0
        l += 1 + self.maxDepth(root.left)
        r += 1 + self.maxDepth(root.right)
        return max(l ,r)