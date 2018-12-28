# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def count(self, l):
        counta = 0
        while l != None:
            counta +=1
            l = l.next
        return counta

    def add(self, l1, l2):
        if l1.next is None and l2.next is None:
            l1.val += l2.val
            if l1.val > 9:
                l1.val -= 10
                return 1
            return 0
        extra = self.add(l1.next, l2.next)
        l1.val += l2.val
        if extra == 1:
            l1.val += 1
        if l1.val > 9:
            l1.val -= 10
            return 1
        return 0

    def addextra(self, temp, diff):
        if diff == 1:
            temp.val += 1
            if temp.val>9:
                temp.val -= 10
                return 1
            return 0
        extra = self.addextra(temp.next, diff-1)
        if extra == 1:
            temp.val += 1
        if temp.val > 9:
            temp.val -= 10
            return 1
        return 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count1 = self.count(l1)
        count2 = self.count(l2)
        temp = None
        diff = abs(count1 - count2)
        if count1 >= count2:
            temp = l1
            while count1-count2 != 0:
                l1 = l1.next
                count1 -= 1
        elif count1 < count2:
            temp = l2
            while count2-count1 != 0:
                l2 = l2.next
                count2 -= 1
        extra = self.add(l1, l2)
        if diff == 0:
            if extra == 1:
                tempe = ListNode(1)
                tempe.next = temp
                temp = tempe
                return temp
            else:
                return temp
        else:
            if extra == 1:
                extra = self.addextra(temp, diff)
                if extra == 1:
                    tempe = ListNode(1)
                    tempe.next = temp
                    temp = tempe
                    diff +=1
            tempe = temp
            while diff != 1:
                tempe = tempe.next
                diff -= 1
            tempe.next = l1
            return temp


if __name__ == "__main__":
    s = Solution()
    l = ListNode(9)
    m = ListNode(9)
    # n = ListNode(9)
    # o = ListNode(3)
    p = ListNode(2)
    # q = ListNode(6)
    # r = ListNode(4)
    l.next = m
    # m.next = n
    # n.next = o
    # p.next = q
    # q.next = r
    list1 = s.addTwoNumbers(p, l)
    while list1 != None:
        print(list1.val)
        list1 = list1.next
