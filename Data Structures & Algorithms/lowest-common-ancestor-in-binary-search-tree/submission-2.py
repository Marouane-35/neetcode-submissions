# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        inf=min(p.val,q.val)
        sup=max(p.val,q.val)
        if inf<=root.val<=sup :
            return root
        elif inf<root.val :
            return self.lowestCommonAncestor(root.left,p,q)
        else :
            return self.lowestCommonAncestor(root.right,p,q)