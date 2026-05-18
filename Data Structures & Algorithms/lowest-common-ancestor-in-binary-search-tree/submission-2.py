# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Case 1: if p is less than root and q is greater, root is lcm
        #Case 2: if both are less than root, then lcm is on root.left
        #Case 3: if both are greater than root, then lcm is on root.right
        #Case 4: if one is equal to root, then lcm is root
        curr = root
        while curr: 
            if q.val < curr.val and p.val < curr.val:
                curr = curr.left
            elif q.val > curr.val and p.val > curr.val:
                curr = curr.right
            else:
                return curr
        
            