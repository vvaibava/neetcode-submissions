# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Breadth first search approach
        #initialize right side of a level to null
        #pop nodes from the left of queue 
        #if nodes arent null, set right side to node, append node.left and right
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            right = None 
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right = node
            if right:
                res.append(right.val)
        return res
