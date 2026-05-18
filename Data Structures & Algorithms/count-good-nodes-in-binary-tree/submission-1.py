# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #recursive dfs helper functions
        #keeping track of max nodes on root.left and right
        #compare node val and max val(root.val), 1 if greater equal else 0
        def dfs(root, maxVal):
            if not root:
                return 0
            good = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)
            return good + dfs(root.left, maxVal) + dfs(root.right, maxVal)
        return dfs(root, root.val)

