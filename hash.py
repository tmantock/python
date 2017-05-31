class Node:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next
    def setNext(self, node):
        self.next = node

class LinkedList:
    def __init__(self):
        self.head = None

    def appendNode(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
            return

        n = self.head

        while n.getNext() is not None:
            n = n.getNext()

        newNode = Node(key, value)
        n.setNext(newNode)

    def removeNode(self, target):
        if self.head is None:
            print "List is not set"
            return

        if self.head.getValue() == target:
            self.head = self.head.getNext()
            return

        current = self.head
        previous = self.head

        while current:
            if current.getValue() == target:
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
            print n.getValue()
            n = n.getNext()

class HashTable:
    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append(LinkedList())

    def element(self, i):
        return i % self.numBuckets
    def insert(self, key, value):
        self.buckets[self.element(key)].appendNode(key, value)
    def printTable(self):
        print self.buckets
    def __str__(self):
        result = '{'
        for b in self.buckets:
            b.traverse()
        #     for e in b:
        #         result = result + str(e[0]) + ':' + str(e[1]) + ','
        # return result[:-1] + '}' #result[:-1] omits the last comma
        return "Printed"

hash = HashTable(5)
hash.insert(1, "John")
hash.printTable()
#hash.insert(5, "John")
print hash