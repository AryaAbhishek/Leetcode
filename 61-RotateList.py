# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        count = 0
        end = head
        while end.next is not None:
            count += 1
            end = end.next
        count += 1
        k %= count
        if k == 0:
            return head
        else:
            i = 1
            temp = head
            while i != count-k:
                temp = temp.next
                i += 1
            end.next = head
            head = temp.next
            temp.next = None
        return head


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    list1 = s.rotateRight(a, 2)
    while list1 is not None:
        print(list1.val)
        list1 = list1.next