class Node(object):
    def __init__(self):
        self._children = [None] * 26
        self._end = False
    
    @property
    def children(self):
        return self._children
    
    @property
    def end(self):
        return self._end
    
    @end.setter
    def end(self, value):
        self._end = value

class Trie(object):
    def __init__(self):
        self._root = Node()
    
    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def _indexToChar(self, index):
        return chr(index + ord('a'))
    
    def insert(self, word):
        root = self._root

        for c in word:
            index = self._charToIndex(c)

            if root.children[index]:
                root = root.children[index]
                root.end = False
            else:
                root.children[index] = Node()
                root = root.children[index]

        root.end = True


    def search(self, word):
        root = self._root

        for c in word:
            index = self._charToIndex(c)

            if not root.children[index]:
                return False
            
            root = root.children[index]
        
        return root is not None and root.end
    
    def _suggestions(self, word = "", index = 0, node = None, results = []):
        if not node:
            return

        if node.end:
            results.append(word)
            return
        
        for i, n in enumerate(node.children):
            if n is not None:
                self._suggestions(word + self._indexToChar(i), i, n, results)
    
    def suggestions(self, word):
        root, result = self._root, []

        for c in word:
            index = self._charToIndex(c)

            if not root.children[index]:
                break
            
            root = root.children[index]
        
        self._suggestions(word, 0, root, result)

        return result
        



t = Trie()
t.insert("hello")
t.insert("helium")
t.insert("hero")

print(t.search("hello"))
print(t.suggestions("he"))
