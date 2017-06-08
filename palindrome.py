##Recurssion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self, data):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next
    def __str__(self):
        return str(self.data)

def reverseList(head):
    current = head.getNext()
    previous = head
    previous.setNext(None)
    while current:
        n = current.getNext()

        current.setNext(previous)
        previous = current
        current = n
    
    return previous

def palindrome(head):
    if head is None and head.getNext() is None:
        return True
    
    track = head
    slow = head
    fast = head

    while slow.getNext() and fast.getNext().getNext():
        slow = slow.getNext()
        fast = fast.getNext().getNext()

    slow = slow.getNext()
    slow = b2 = reverseList(slow)

    while slow and head:
        print slow
        if head.data != slow.data:
            return False
        head = head.getNext()
        slow = slow.getNext()


    reverseList(b2)
    #printList(track)
    return True


def printList(node):
    root = node

    while root:
        print root
        root = root.getNext()

def toChars(s):
    import string
    s = string.lower(s)
    ans = ''
    for c in s:
        if c in string.lowercase:
            ans = ans + c
    return ans

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toChars(s))

# print isPalindrome('Guttag')
# print isPalindrome('Guttug')
# print isPalindrome('Able was I ere I saw Elba')
# print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')

root = Node('g')
n2 = Node('u')
root.setNext(n2)
n3 = Node('t')
n2.setNext(n3)
n4 = Node('t')
n3.setNext(n4)
n5 = Node('u')
n4.setNext(n5)
n6 = Node('g')
n5.setNext(n6)

print palindrome(root)
