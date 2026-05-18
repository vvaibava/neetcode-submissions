# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #bottom up approach --> keep track of each sub tree with the height
        #if the height of two trees is <= 1, then that subtree is balanced
        #height of a subtree is 1 + max(height1, height2)
        #each subtree has a [boolean, height]
        def dfs(curr):
            if not curr:
                return [True, 0]
            left, right = dfs(curr.left), dfs(curr.right)
            
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]