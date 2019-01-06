# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return temp
        return

if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = a.next
    list1 = s.detectCycle(a)
    if list1 is None:
        print("No Cycle")
    else:
        i=0
        while list1 != a:
            a = a.next
            i += 1
        print("cycle at index {}.".format(i))