# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #helper function to check if trees are the same. 
        #recursively look through left and right in main function
        #edge cases: is one of the trees null, is the tree not a leaf node
        #            if t is exists, return True, or if s does not exist, return False
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
        
    def sameTree(self, s, t):
        if not s and not t: 
            return True
        
        if s and t and s.val == t.val:
            equals = (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))
            return equals
        return False
            