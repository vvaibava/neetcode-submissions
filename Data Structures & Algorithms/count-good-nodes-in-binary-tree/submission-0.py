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
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            res += dfs(node.left, max(maxVal, node.val))
            res += dfs(node.right, max(maxVal, node.val))
            return res

        return dfs(root, root.val)
                    
