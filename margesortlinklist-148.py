# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sort(self, lhead, rhead):
        head = None
        temp = None
        if lhead.val>=rhead.val:
            head = rhead
            rhead = rhead.next
        else:
            head = lhead
            lhead = lhead.next
        temp = head
        while lhead != None and rhead != None:
            if lhead.val>=rhead.val:
                temp.next = rhead
                rhead = rhead.next
            else:
                temp.next = lhead
                lhead = lhead.next
            temp = temp.next
        if lhead != None:
            while lhead!= None:
                temp.next = lhead
                lhead = lhead.next
                temp = temp.next
        elif rhead != None:
            while rhead!= None:
                temp.next = rhead
                rhead = rhead.next
                temp = temp.next
        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None:
            return head
        end = head
        start = head
        while end.next != None:
            if end.next != None and end.next.next != None:
                end = end.next.next
                start = start.next
            elif end.next != None:
                end = end.next
        rstart = start.next
        start.next = None
        return self.sort(self.sortList(head), self.sortList(rstart))

if __name__ == "__main__":
    s = Solution()
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    s.sortList(a)