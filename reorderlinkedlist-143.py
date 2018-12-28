# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        start = head
        end = head
        while end.next != None:
            if end.next != None and end.next.next != None:
                end = end.next.next
                start = start.next
            else:
                end = end.next
        rhead = start.next
        start.next = None
        start = head
        flag = False
        while start != None:
            if flag == False:
                flag = True
                if rhead != None:
                    temp = rhead
                    prev = None
                    while temp.next != None:
                        prev = temp
                        temp = temp.next
                    temp.next = start.next
                    start.next = temp
                    if prev != None:
                        prev.next = None
                    else:
                        rhead = None
            else:
                flag = False
            start = start.next

if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    # e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    # d.next = e
    r = s.reorderList(a)
    while a != None:
        print(a.val)
        a = a.next