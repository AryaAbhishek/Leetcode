# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def same(self, root, val):
        if root is None:
            return True
        if root.val == val:
            if root.left is None and root.right is None:
                return True
            return self.same(root.left, val) and self.same(root.right, val)
        return False
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.same(root, root.val)


if __name__ == "__main__":
    t = TreeNode(10)
    t.left = TreeNode(10)
    t.right = TreeNode(10)
    s = Solution()
    print(s.isUnivalTree(t))

