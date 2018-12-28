# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is None and l2 is None) or l2 is None:
            return l1
        elif l1 is None:
            return l2
        extra = 0
        temp1 = l1
        while temp1.next != None and l2.next != None:
            if extra == 1:
                temp1.val += extra
                extra = 0
            temp1.val += l2.val
            if temp1.val>9:
                temp1.val -= 10
                extra = 1
            temp1 = temp1.next
            l2 = l2.next
        if extra == 1:
            temp1.val += extra
            extra = 0
        temp1.val += l2.val
        if temp1.next == None and l2.next == None:
            if temp1.val>9:
                temp1.val -= 10
                temp1.next = ListNode(1)
            return l1
        elif temp1.next == None:
            if temp1.val>9:
                temp1.val -= 10
                extra = 1
            l2 = l2.next
            while l2 != None:
                temp1.next = ListNode(l2.val)
                temp1 = temp1.next
                if extra == 1:
                    temp1.val += extra
                    extra = 0
                if temp1.val>9:
                    temp1.val -= 10
                    extra = 1
                l2 = l2.next
            if extra == 1:
                temp1.next = ListNode(1)
            return l1
        elif l2.next == None:
            if temp1.val>9:
                temp1.val -= 10
                extra = 1
            temp1 = temp1.next
            while temp1.next != None:
                if extra == 1:
                    temp1.val += 1
                    extra = 0
                if temp1.val>9:
                    temp1.val -= 10
                    extra = 1
                temp1 = temp1.next
            if extra == 1:
                temp1.val += extra
                extra = 0
                if temp1.val>9:
                    temp1.val -= 10
                    temp1.next = ListNode(1)
            return l1