class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getNext(self):
        return self.next
    def setNext(self, node):
        self.next = node
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.head = None
    """
    Insert nodes to the top of the Stack
    Cannot be inserted at the end
    """
    def push(self, data):
        head = self.head
        node = Node(data)

        if head is None:
            self.head = node
            return

        node.setNext(head)
        self.head = node
    """
    Pull nodes off the top of the stack
    """
    def pop(self):
        if self.head is None:
            return

        head = self.head
        next = head.getNext()
        self.head = next

        return head
    """
    See the first node in the Stack
    """
    def peek(self):
        return self.head
    """
    Print the nodes in a stack
    """
    def showStack(self):
        if self.head is None:
            return

        current = self.head

        while current is not None:
            print current
            current = current.getNext()

s = Stack()
s.push(4)
s.push(5)
s.push(34)
s.push(9)
s.showStack()
print "================"
s.pop()
s.showStack()
print "================"