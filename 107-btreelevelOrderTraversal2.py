# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def order(self, list1, child):
        temp1 = []
        temp2 = []
        for i in child:
            if i.left:
                temp1.append(i.left.val)
                temp2.append(i.left)
            if i.right:
                temp1.append(i.right.val)
                temp2.append(i.right)
        if len(temp1)>0:
            list1.insert(0,temp1)
            return self.order(list1, temp2)
        return list1
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list1 = []
        list2 = []
        if root is None:
            return list1
        list1.append([root.val])
        list2.append(root)
        return self.order(list1, list2)