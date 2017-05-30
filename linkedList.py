class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, node):
        self.next = node

class LinkedList:
    def __init__(self):
        self.head = None

    def appendNode(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        n = self.head

        while n.getNext() is not None:
            n = n.getNext()

        newNode = Node(data)
        n.setNext(newNode)

    def removeNode(self, target):
        if self.head is None:
            print "List is not set"
            return

        if self.head.getData() == target:
            self.head = self.head.getNext()
            return

        current = self.head
        previous = self.head

        while current:
            if current.getData() == target:
                previous.setNext(current.getNext())
                break
            else:
                previous = current
                current = current.getNext()

    def traverse(self):
        if self.head is None:
            print "List not set"
            return

        n = self.head

        while n:
            print n.getData()
            n = n.getNext()

    def reverse(self):
        if self.head is None or self.head.getNext() is None:
            return

        current = self.head.getNext()
        previous = self.head
        previous.setNext(None)

        while current:
            n = current.getNext()

            current.setNext(previous)
            previous = current
            current = n

        self.head = previous




def testList():
    linked = LinkedList()
    linked.appendNode("John")
    linked.appendNode("Shepherd")
    linked.appendNode("Ryder")
    linked.reverse()
    linked.traverse()
    linked.removeNode("Shepherd")
    linked.traverse()

testList()