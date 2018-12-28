class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data=newData

    def setNext(self, item):
        self.next = item


class Unordered:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        flag = False
        while current is not None and not flag:
            if current.getData() == item:
                flag = True
            else:
                current = current.getNext()
        return flag

    def remove(self, item):
        current = self.head
        previous = None
        flag = False
        while not flag:
            if current.getData() == item:
                flag = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        try:
            current = self.head
            flag = False
            count = 0
            while not flag:
                if current.getData() == item:
                    flag = True
                else:
                    count += 1
                    current = current.getNext()
            return count
        except AttributeError:
            return "Number not in list."

    def append(self, item):
        current = self.head
        flag = False
        while not flag:
            if current.getNext() is None:
                current.setNext(item)
                flag = True
            else:
                current = current.getNext()


obj = Unordered()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
print(obj.size())
print(obj.search(3))
print(obj.head.getNext().getNext().getData())
obj.remove(3)
print(obj.search(3))
print(obj.index(2))
obj.append(6)
print(obj.index(6))