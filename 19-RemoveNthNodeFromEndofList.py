# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = None
        fast = head
        for _ in range(n - 1):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            if slow is None:
                slow = head
            else:
                slow = slow.next
        if slow is None:
            head = head.next
        else:
            slow.next = slow.next.next
        return head
#         2 - Pass
#         if head is None:
#             return head
#         count = 1
#         temp = head
#         while temp is not None:
#             temp = temp.next
#             count += 1
#         temp = head
#         prev = None
#         while count-n != 1:
#             prev = temp
#             temp = temp.next
#             count -= 1
#         if prev is not None:
#             prev.next = temp.next
#         if temp == head:
#             head = temp.next
#         temp.next = None
#         return head


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(3)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(4)
    list1 = s.removeNthFromEnd(a, 2)
    while list1 is not None:
        print(list1.val)
        list1 = list1.next