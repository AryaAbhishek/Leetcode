# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None or head.next.next is None:
            return head
        end = head
        count = 0
        while end.next != None:
            end = end.next
            count += 1
        count += 1
        temp = head
        prev = head
        i = 1
        while i<=count:
            if i%2 == 0:
                prev.next = temp.next
                temp.next = None
                end.next = temp
                end = temp
                temp = prev.next
            else:
                prev = temp
                temp = temp.next
            i += 1
        return head


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    list1 = s.oddEvenList(a)
    while list1 is not None:
        print(list1.val)
        list1 = list1.next