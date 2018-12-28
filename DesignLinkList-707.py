class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        """
        Initialize your data structure here.
        """

    def get(self, index):
        temp = self.head
        while temp != None:
            if index == 0:
                return temp.val
            temp = temp.next
            index -= 1
        return -1
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

    def addAtHead(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """

    def addAtTail(self, val):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(val)
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """

    def addAtIndex(self, index, val):
        temp = self.head
        if index == 0:
            self.addAtHead(val)
        while index != 1:
            if temp != None:
                index -= 1
                temp = temp.next
            else:
                break
        if index == 1 and temp != None:
            temp1 = Node(val)
            temp1.next = temp.next
            temp.next = temp1
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """

    def deleteAtIndex(self, index):
        temp = self.head
        while index != 1:
            if temp != None:
                index -= 1
                temp = temp.next
            else:
                break
        if index == 1:
            if temp != None and temp.next != None:
                temp1 = temp.next.next
                temp.next.next = None
                temp.next = temp1
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(0)
print(param_1)
obj.addAtHead(1)
param_2 = obj.get(0)
print(param_2)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.deleteAtIndex(0)