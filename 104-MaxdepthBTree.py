# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth(self, root, d):
        d1, d2 = 0, 0
        if root.left is None and root.right is None:
            return d
        if root.left is not None:
            d1 = self.depth(root.left, d+1)
        if root.right is not None:
            d2 = self.depth(root.right, d+1)
        return max(d1, d2)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.depth(root, 1)