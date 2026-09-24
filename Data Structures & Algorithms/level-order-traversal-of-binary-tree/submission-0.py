# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queu=deque([root])
        while queu :
            level=len(queu)
            current_level=[]
            for _ in range(level) :
                node=queu.popleft()
                current_level.append(node.val)
            
                if node.left :
                    queu.append(node.left)
                if node.right :
                    queu.append(node.right)

            result.append(current_level)
            
        return result