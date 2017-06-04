class Node:
    def __init__(self, data):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;
    def setLeftChild(self, left):
        self.leftChild = left
    def setRigthChild(self, right):
        self.rightChild = right
    def getLeft(self):
        return self.leftChild
    def getRight(self):
        return self.rightChild
    def getData(self):
        return self.data

class Tree:
    def __init__(self, data):
        self.root = Node(data)
    def search(self, data):
        return self.recurseSearch(self.root, data)
    def recurseSearch(self, node, data):
        if data == node.getData():
            return node
        if data > node.getData():
            return self.recurseSearch(node.getRight(), data)
        if data < node.getData():
            return self.recurseSearch(node.getLeft(), data)
    def appendNode(self, data): 
        self.recurseAppend(self.root, data)
    def recurseAppend(self, node, data):
        if node is None:
            return Node(data)
        if data > node.getData():
            node.setRigthChild(self.recurseAppend(node.getRight(), data))
        if data < node.getData():
            node.setLeftChild(self.recurseAppend(node.getLeft(), data))

        return node
    def traverseTree(self):
        self.recurseTree(self.root)
    def recurseTree(self, node):
        if node is not None:
            print node.getData()
            self.recurseTree(node.getLeft())
            self.recurseTree(node.getRight())

t = Tree(1)
t.appendNode(10)
t.appendNode(3)
t.appendNode(4)
t.traverseTree()
f = t.search(10)
print f