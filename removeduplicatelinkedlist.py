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
        if head == None or head.next == None:
            return head
        temp = head.next
        prev = head
        while temp != None:
            if prev.val != temp.val:
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next
                temp.next = None
                temp = prev.next
        return head


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(4)
    e = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    r = s.deleteDuplicates(a)
    while a != None:
        print(a.val)
        a = a.next