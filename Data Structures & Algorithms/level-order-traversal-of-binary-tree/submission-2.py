# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #breadth first search
        #initalize a deque and append the root
        #while the queue is non empty, loop through values within the q(iter 1 level at a time)
        #pop nodes from the left of the queue
        #append it to the list if it is not null, then append the children of that node
        #append the list to the result list
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

        