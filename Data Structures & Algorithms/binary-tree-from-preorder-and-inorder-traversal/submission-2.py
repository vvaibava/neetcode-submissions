# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #first val in preorder is gonna be the root
        #every val left of root in in order is left subtree, and
        #every val right of root is right subtree
        #find length of left and right sub array --> allow to partition pre order 
        #left subtree is recursive implementation of (preorder[1:mid + 1], inorder[:mid])
        #right subtree is recursive implementation (preorder[mid + 1], inorder[mid+1:])
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root