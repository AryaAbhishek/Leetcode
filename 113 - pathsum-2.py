# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def path(self, root, sum, total, arr):
        list1 = []
        if root is None:
            return []
        if root.left is None and root.right is None:
            if sum == total + root.val:
                arr.append(root.val)
                return [arr]
            else:
                return []
        if root.left:
            arr1 = arr[:]
            arr1.append(root.val)
            list1.extend(self.path(root.left, sum, total+root.val, arr1))
        if root.right:
            arr2 = arr[:]
            arr2.append(root.val)
            list1.extend(self.path(root.right, sum, total + root.val,arr2))
        return list1
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        list1 = []
        if root is None:
            return list1
        if root.left is None and root.right is None:
            if sum - root.val == 0:
                list1.append(root.val)
                return [list1]
        list1.extend(self.path(root.left, sum, root.val, [root.val]))
        list1.extend(self.path(root.right, sum, root.val, [root.val]))
        return list1