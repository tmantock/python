class Node:
    def __init__(self, data, parent = None):
        self.data = data
        self.children = []
        self.parent = parent
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
    def setParent(self, parent):
        self.parent = parent
    def offer(self):
        return len(self.children) < 2
    def addChild(self, node, parent):
        if len(self.children) == 2:
            raise ValueError("Max Children.")
        else:
            node.setParent(parent)
            self.children.append(node)
    def getChildren(self):
        return self.children
    def getParent(self):
        return self.parent
    def removeChild(self, node):
        del self.children[self.children.index(node)]
    def printNode(self):
        print self
        if len(self.children) == 1:
            self.children[0].printNode()
        if len(self.children) == 2:
            self.children[0].printNode()
            self.children[1].printNode()
    def __str__(self):
        return "I am " + str(self.data) + " Parent is " + str(self.parent.data if self.parent is not None else None)

class MinHeap:
    def __init__(self, root):
        self.root = Node(root)
        self.last = None
    def append(self, node):
        root = self.root
        node = Node(node)

        if root is None or node is None:
            return

        while root:
            if root.offer():
                root.addChild(node, root)
                self.heapifyUp(node)
                self.last = node
                break
            else:
                left = root.getChildren()[0]
                right = root.getChildren()[1]

                if left.offer():
                    root = left
                else:
                    root = right

    def swap(self, a, b):
        if a is None or b is None:
            return

        temp = a.getData()
        a.setData(b.getData())
        b.setData(temp)

    def heapifyUp(self, node):
        if node is None or node.getParent() is None:
            return
        parent = node.getParent()
        if parent.getData() > node.getData():
            self.swap(node, node.getParent())
            self.heapifyUp(node.getParent())
        else:
            return
    def heapifyDown(self, node):
        if node is None:
            return
        if len(node.getChildren()) == 0:
            return
        ch = node.getChildren()
        if len(ch) == 1:
            left = ch[0]
            if node.getParent() < left.getData():
                return
            else:
                self.swap(node, left)
                self.heapifyDown(left)
        elif len(ch) == 2:
            left = ch[0]
            right = ch[1]

            if right.getData() < left.getData():
                min = right
            else:
                min = left
            if node.getData() > min.getData():
                self.swap(node, min)
                self.heapifyDown(min)
    def removeMin(self):
        if self.root is None or self.last is None:
            return
        node = self.root
        self.root.setData(self.last.getData())
        self.last.getParent().removeChild(self.last)
        self.heapifyDown(self.root)
        return node
    def traverse(self):
        self.root.printNode()


def testHeap():
    h = MinHeap(5)
    h.append(10)
    h.append(100)
    h.append(4)
    h.append(8)
    h.append(9)
    h.append(1)
    # h.append(16)
    h.traverse()
    h.removeMin()
    print "--------------"
    h.traverse()

testHeap()