import math

class Savings(object):
    def __init__(self, user):
        self.user = user
        self. purchases = {}
        self.totalSavings = 0;
    def Purchase (self, product, price):
        assert type(price) == float
        self.purchases[product] = math.ceil(price) - price
        self.totalSavings += sef.purchases[product]
        return self.purchases[product]

matt = Savings("Matt")
print Mac.Purchase("Mac", 3253.23)
