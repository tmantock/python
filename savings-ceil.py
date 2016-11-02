import math

class Savings(object):
    def __init__(self, name):
        self.name = name
        self. purchases = {}
    def Purchase (self, name, price):
        assert type(price) == float
        self.purchases[name] = math.ceil(price) - price
        return self.purchases[name]

Mac = Savings("Mac")
print Mac.Purchase("Mac", 3253.23)
