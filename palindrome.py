##Recurssion
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

def IsPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toChars(s))

# print isPalindrome('Guttag')
# print isPalindrome('Guttug')
# print isPalindrome('Able was I ere I saw Elba')
# print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')

root = Node("g")
n1 = Node("u")
root.setNext(n1)
n2 = Node("t")
n1.setNext(n2)
n3 = Node("t")
n2.setNext(n3)
n4 = Node("u")
n3.setNext(n4)
n5 = Node("g")
n4.setNext(n5)

isPalindrome(root)