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
        if self.data <= data:
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

    def __str__(self):
        return "( " + str(self.position) + ", " + str(self.data) + ")"

root = Node(5)
root.insert(4)
root.insert(7)
root.insert(3)
# print root.find(8)
root.printInOrder()