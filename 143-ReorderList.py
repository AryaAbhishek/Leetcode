# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        slow = head
        fast = head
        while fast.next != None:
            if fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            else:
                fast = fast.next
        temph = slow.next
        slow.next = None
        temp = temph
        while temp.next is not None:
            temp1 = temp.next
            temp.next = temp1.next
            temp1.next = temph
            temph = temp1
        slow.next = temph
        temp = head
        flag = False
        while temp != slow and temph is not None:
            if not flag:
                flag = True
                temp1 = temph
                temph = temph.next
                temp1.next = temp.next
                temp.next = temp1
                temp = temp.next
                slow.next = temph
            else:
                flag = False
                temp = temp.next


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    s.reorderList(a)
    while a is not None:
        print(a.val)
        a = a.next