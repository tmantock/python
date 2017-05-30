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

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
        self.max = 10

    def enqueue(self, n):
        if self.count == self.max:
            print "Max reached. Sorry %s" %n
            print "\n"
            return

        self.count += 1

        nd = Node(n)

        if self.first is None:
            self.first = nd
            return

        if self.first is not None and self.last is None:
            self.first.setNext(nd)
            self.last = nd
            return

        self.last.setNext(nd)
        self.last = nd

    def dequeue(self):
        if self.first is None:
            print "Que is empty"
            return

        n = self.first.getNext()
        self.first.setNext(None)
        self.first = n
        self.count -= 1

    def peek(self):
        return self.first.getData()

    def offer(self):
        if self.max != self.count:
            return True
        return False

    def traverse(self):
        if self.first is None:
            return

        n = self.first

        while n:
            print n.getData()
            n = n.getNext()

def testQue():
    que = Queue()
    que.enqueue("Jenny")
    que.enqueue("James")
    que.enqueue("Jeremy")
    que.enqueue("Claire")
    que.enqueue("John")
    que.enqueue("Peter")
    que.enqueue("Melanie")
    que.enqueue("Jennifer")
    que.enqueue("Zoey")
    que.enqueue("Barnes")
    que.enqueue("Frank")
    que.traverse()
    print "\n \n"
    que.dequeue()
    que.traverse()
    print "\n \n"
    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()

    if que.offer():
        que.enqueue("Frank")

    print "\n \n"
    que.traverse()

testQue()