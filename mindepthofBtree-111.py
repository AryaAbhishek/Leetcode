# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth(self, root, d):
        if root is None:
            return d
        if root.left and root.right:
            return min(self.depth(root.left, d + 1), self.depth(root.right, d + 1))
        elif root.left:
            return self.depth(root.left, d + 1)
        elif root.right:
            return self.depth(root.right, d + 1)
        else:
            return d + 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root, 0)
