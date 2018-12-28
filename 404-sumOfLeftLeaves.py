# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        total1, total2 = 0, 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                total1 = root.left.val
            total1 += self.sumOfLeftLeaves(root.left)
        if root.right:
            total2 = self.sumOfLeftLeaves(root.right)
        return total1 + total2