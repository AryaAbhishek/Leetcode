# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            root = root
        elif root.left == None and root.right == None:
            root = root
        else:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left != None:
                temp = root.right
                root.right = root.left
                root.left = None
                left = root.right
                while left.right != None:
                    left = left.right
                left.right = temp

if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = e
    b.left = c
    b.right = d
    e.right = f
    s.flatten(a)
    while a != None:
        print(a.val)
        a = a.left