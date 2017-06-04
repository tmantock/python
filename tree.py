class Node:
    def __init__(self, data, position = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.position = position

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
    def setData(self, data):
        self.data = data
    def setPosition(self, pos):
        self.position = pos
    def __str__(self):
        return "( " + str(self.position) + ", " + str(self.data) + ")"

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)
    def search(self, data):
        return self.recurseSearch(self.root, data)
    def recurseSearch(self, node, data):
        if node is None:
            return
        if data == node.getData():
            return node
        if data > node.getData():
            return self.recurseSearch(node.getRight(), data)
        if data < node.getData():
            return self.recurseSearch(node.getLeft(), data)
    def appendNode(self, data):
        self.recurseAppend(self.root, data)
    def recurseAppend(self, node, data, position = None):
        if node is None:
            return Node(data, position)
        if data > node.getData():
            node.setRigthChild(self.recurseAppend(node.getRight(), data, 'Right'))
        if data < node.getData():
            node.setLeftChild(self.recurseAppend(node.getLeft(), data, 'Left'))
        return node
    def preOrderTraverseTree(self):
        self.preOrderRecurseTree(self.root)
    def preOrderRecurseTree(self, node):
        if node is not None:
            print node
            self.preOrderRecurseTree(node.getLeft())
            self.preOrderRecurseTree(node.getRight())
    def swap(self, node1, node2):
        temp = node1.getData()
        node1.setData(node2.getData())
        node2.setData(temp)


t = BinarySearchTree(1)
t.appendNode(10)
t.appendNode(3)
t.appendNode(4)
t.preOrderTraverseTree()
# f = t.search(10)
# print f