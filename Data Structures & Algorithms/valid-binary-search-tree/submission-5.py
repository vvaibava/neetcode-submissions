# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #recursive dfs through both branches
        #initialize large negative and positive for left and right vals
        #if num is not in between those two, return false
        #left: -inf > val > prev.val , right: prev.val< val < inf
        def dfs(left, root, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            return dfs(left, root.left, root.val) and dfs(root.val, root.right, right)
        return dfs(float("-inf"), root, float("inf"))
