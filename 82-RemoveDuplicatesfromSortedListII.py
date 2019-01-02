# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        temp = head
        prev = None
        val = float("inf")
        while temp.next is not None:
            if temp.val == temp.next.val or temp.val == val:
                val = temp.val
                if temp == head:
                    prev = temp
                    temp = temp.next
                    prev.next = None
                    prev = None
                    head = temp
                else:
                    prev.next = temp.next
                    temp.next = None
                    temp = prev.next
            else:
                prev = temp
                temp = temp.next
        if temp.val == val:
            if prev is not None:
                prev.next = None
            if head == temp:
                head = None
        return head


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(3)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(2)
    a.next.next.next.next = ListNode(4)
    list1 = s.deleteDuplicates(a)
    while list1 is not None:
        print(list1.val)
        list1 = list1.next