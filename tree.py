class Node:
    def __init__(self, data, position = None):
        self.data = data
        self.left = None
        self.right = None
        self.position = position
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getData(self):
        return self.data
    def insert(self, data):
        if self.data >= data:
            if self.left is None:
                self.left = Node(data, 'Left')
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data, 'Right')
            else:
                self.right.insert(data)
    def find(self, data):
        if self.data == data:
            return self
        if self.data < data and self.left is not None:
            return self.left.find(data)
        elif self.data > data and self.right is not None:
            return self.right.find(data)

        return False
    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print self
        if self.right is not None:
            self.right.printInOrder()
    def printPreOrder(self):
        print self
        if self.left is not None:
            self.left.printPreOrder()
        if self.right is not None:
            self.right.printPreOrder()
    def printPostOrder(self):
        if self.left is not None:
            self.left.printPreOrder()
        if self.right is not None:
            self.right.printPreOrder()
        print self
    def BFS(self):
        queue = [self]
        while queue:
            root = queue.pop(0)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            print root
    def DFS(self):
        nodes = []
        stack = [self]
        while stack:
            root = stack.pop(0)
            nodes.append(root)
            if root.left:
                stack.insert(0, root.left)
            if root.right:
                stack.insert(0, root.right)
        for n in nodes:
            print n
    def __str__(self):
        return "( " + str(self.position) + ", " + str(self.data) + ")"

root = Node(5)
root.insert(4)
root.insert(7)
root.insert(3)
root.insert(5)
root.insert(6)
print root.find(8)
print "```````````````````"
root.printInOrder()
print "```````````````````"
root.printPreOrder()
print "```````````````````"
root.printPostOrder()
print "---------------------"
root.BFS()
print "*********************"
root.DFS()
