class HashTable:
    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def element(self, i):
        return i % self.numBuckets
    def insert(self, key, value):
        self.buckets[self.element(key)].append((key, value))
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' #result[:-1] omits the last comma

hash = HashTable(5)
hash.insert(5, "John")
print hash