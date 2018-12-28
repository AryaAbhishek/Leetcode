# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def check(self, left, right):
        if left and right:
            if left.val == right.val:
                temp1 = self.check(left.left, right.right)
                temp2 = self.check(left.right, right.left)
                return temp1 and temp2
        return left == right
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.check(root.left, root.right)
        return True