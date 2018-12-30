# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def frequent(self, root):
        list1 = []
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        temp = root.val
        if root.left:
            list2 = self.frequent(root.left)
            list1.extend(list2)
            temp += list2[-1]
        if root.right:
            list3 = self.frequent(root.right)
            list1.extend(list3)
            temp += list3[-1]
        list1.append(temp)
        return list1
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1 = self.frequent(root)
        dict1 = {}
        temp = 0
        for i in list1:
            if i not in dict1:
                dict1[i] = list1.count(i)
                if dict1[i]>temp:
                    temp = dict1[i]
        list2 = []
        for i in dict1:
            if dict1[i] == temp:
                list2.append(i)
        return list2