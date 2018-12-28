class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        temp = head
        count = 1
        temp1, temp2, prev = ListNode(0), ListNode(0), ListNode(0)
        while temp != None:
            if count == m-1:
                temp1 = temp
            elif count == m:
                temp2 = temp
            if count > m and count <n+1:
                temp1.next = temp
                prev.next = temp.next
                temp.next = temp2
                temp2 = temp
                temp = prev
            count += 1
            temp = temp.next
        return head


if __name__ =="__main__":
    s = Solution()
    l = ListNode(1)
    m = ListNode(2)
    n = ListNode(3)
    o = ListNode(4)
    p = ListNode(5)
    l.next = m
    m.next = n
    n.next = o
    o.next = p
    print(s.reverseBetween(l, 2, 4))