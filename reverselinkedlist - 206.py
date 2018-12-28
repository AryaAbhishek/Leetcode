# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return []
        current = head.next
        previous = head
        while current is not None:
            previous.next = current.next
            current.next = head
            head = current
            current = previous.next
        return head