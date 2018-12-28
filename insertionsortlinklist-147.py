# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        temp = head
        prev = ListNode(0)
        count = 0
        flag = False
        while temp != None:
            if count == 0:
                prev = temp
                temp = temp.next
            else:
                if temp.val >= prev.val:
                    prev = prev.next
                    temp = temp.next
                    print(temp.val, prev.val)
                elif temp.val <= head.val:
                    prev.next = temp.next
                    temp.next = head
                    head = temp
                    flag = True
                    print(head.val, prev.val, temp.val)
                else:
                    temp1 = head.next
                    prev1 = head
                    print("temp",head.val, prev.val, temp.val)
                    while temp1 != None:
                        print("temp1", head.val, prev1.val, temp1.val)
                        if temp.val <= temp1.val:
                            prev.next = temp.next
                            prev1.next = temp
                            temp.next = temp1
                            flag = True
                            break
                        temp1 = temp1.next
                        prev1 = prev1.next
            count += 1
            if flag:
                temp = prev.next
                flag = False
        return head


if __name__ == "__main__":
    s = Solution()
    a = ListNode(-1)
    b = ListNode(5)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(0)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    r = s.insertionSortList(a)
    while r != None:
        print(r.val)
        r = r.next
