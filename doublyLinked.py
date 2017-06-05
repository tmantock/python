class Node:
    def __init__(self, data, prev = None):
        self.data = data
        self.next = None
        self.prev = prev
    def getData(self, data):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def setNext(self, next):
        self.next = next
    def setPrev(self, prev):
        self.prev = prev
    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        if self.tail is not None:
            self.tail.setNext(node)
            self.tail = node
        else:
            self.head.setNext(node)
            self.tail = node

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        node = Node(data)
        self.head.setPrev(node)
        node.setNext(self.head)
        self.head = node
    def printList(self):
        if self.head is None:
            return

        current = self.head

        while current is not None:
            print current
            current = current.getNext()

dl = DoublyLinkedList()
dl.append(2)
dl.append(15)
dl.append(43)
dl.printList()
print "--------------------"
dl.push(55)
print "--------------------"
dl.printList()