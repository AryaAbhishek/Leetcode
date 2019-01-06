# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = None
        prev = ListNode(0)
        prev.next = head
        dummy = ListNode(0)
        dummy.next = prev
        while head is not None and head.next is not None:
            temp = head.next
            head.next = head.next.next
            temp.next = head
            prev.next = temp
            prev = head
            head = head.next
        return dummy.next.next


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    list1 = s.swapPairs(a)
    while list1 is not None:
        print(list1.val)
        list1 = list1.next