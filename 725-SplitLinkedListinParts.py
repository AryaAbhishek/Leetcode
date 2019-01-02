# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        temp = root
        list1 = []
        while temp is not None:
            temp = temp.next
            length += 1
        if length // k == 0:
            temp = root
            while temp is not None:
                temp1 = temp
                temp = temp.next
                temp1.next = None
                list1.append(temp1)
                k -= 1
            while k != 0:
                list1.append(temp)
                k -= 1
        else:
            extra = length % k
            temp = root
            tempv = 1
            while temp is not None:
                if tempv == length // k:
                    if extra > 0:
                        temp = temp.next
                        extra -= 1
                    temp1 = temp
                    temp = temp.next
                    temp1.next = None
                    list1.append(root)
                    root = temp
                    tempv = 1
                else:
                    temp = temp.next
                    tempv += 1
        return list1


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(3)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(4)
    list1 = s.splitListToParts(a, 3)
    for list2 in list1:
        while list2 is not None:
            print(list2.val)
            list2 = list2.next
        print("\n")