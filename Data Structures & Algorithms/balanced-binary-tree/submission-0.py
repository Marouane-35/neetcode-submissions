# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return (abs(self.depth(root.left) - self.depth(root.right)) <= 1 
                and self.isBalanced(root.left) 
                and self.isBalanced(root.right))

    def depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        return 1 + max(left_depth, right_depth)