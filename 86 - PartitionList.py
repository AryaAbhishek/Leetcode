# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        temph = None
        temp = head
        prev = head
        while temp is not None:
            if temp.val < x:
                if temph is None:
                    if temp == head:
                        temph = temp
                        prev = temp
                        temp = temp.next
                    elif temp != head:
                        temph = temp
                        temp = temp.next
                        prev.next = temp
                        temph.next = head
                        head = temph
                else:
                    if prev == temph:
                        temph = temp
                        prev = temp
                    else:
                        prev.next = temp.next
                        temp.next = temph.next
                        temph.next = temp
                        temph = temp
                    temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return head

if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(3)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(4)
    list1 = s.partition(a, 3)
    while list1 is not None:
        print(list1.val)
        list1 = list1.next