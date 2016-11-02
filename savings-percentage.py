class Savings(object):
	def __init__(self, perc):
		assert type(perc) == float
		self.perc = perc
		self.purchases = {}
	def Purchase(self, name, item, amount):
		assert type(item) == float
		assert type(amount) == float
	
		exchange = amount - item
		self.purchases[name] = exchange
		return exchange
	def SaveAmount(self, item):
		savings = self.purchases[item] * self.perc
		return savings
		
mac = Savings(0.02)
mac.Purchase("Mac", 3000.00, 3250.00)
print mac.SaveAmount("Mac")
