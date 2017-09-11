class Node(object):
    def __init__(self, data, left = None, right = None, parent = None, height = 0):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.height = height
    def getRight(self):
        if self.right is None:
            return -1
        else:
            return self.right.height
    def getLeft(self):
        if self.left is None:
            return -1
        else:
            return self.left.height
    def setHeight(self):
        self.height = max(self.getLeft(), self.getRight()) + 1
    def append(self, data):
        if data < self.data:
            """Go left"""
            if self.left is None:
                self.left = Node(data, parent = self)
            else:
                self.left.append(data)
        else:
            """Go Right"""
            if self.right is None:
                self.right = Node(data, parent = self)
            else:
                self.right.append(data)
        if self.getLeft() - self.getRight() == 2:
            self.rebalance()
        # Recalculate the height
        self.setHeight()
    def rebalance(self):
        self.setHeight()
        if self.getLeft >= 2 + self.getRight():
            if self.getLeft() >= self.getRight():
                self.rotateRight()
            else:
                self.left.rotateLeft()
                self.rotateRight()
        elif self.getRight() >= 2 + self.getLeft():
            if self.getRight() >= self.getLeft():
                self.rotateLeft()
            else:
                self.right.rotateRight()
                self.rotateLeft()
        self = self.parent

    def rotateLeft(self):
        self, self.left = self.left, self
        self.left.setHeight()
        self.setHeight()

    def doubleRotateLeft(self):
        self, self.right, self.right.left = self.right, self.right.left, self
        self.left.setHeight()
        self.setHeight()

    def rotateRight(self):
        self, self.right = self.right, self
        self.right.setHeight()
        self.setHeight()

    def doubleRotateRight(self):
        self, self.left, self.left.right = self.left, self.left.right, self
        self.right.setHeight()
        self.setHeight()

    def inOrderTraverse(self):
        if self.left is not None:
            self.left.inOrderTraverse()
        print self, self.height
        if self.right is not None:
            self.right.inOrderTraverse()
    def __str__(self):
        return str(self.data)
class AVL(object):
    def __init__(self):
        self.root = None
    def append(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.append(data)
    def printTree(self):
        self.root.inOrderTraverse()


a = AVL()
a.append(6)
a.append(8)
a.append(4)
a.append(3)
a.append(9)
a.append(1)
a.printTree()