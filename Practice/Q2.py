class Product:
	def __init__(self, category):
		self.category = category
	def cal_tax(self):
		if self.category == "book":
			tax = 0
		else:
			tax = 5
		return tax
		
p1 = Product("book")
p2 = Product("mobile")
p1.cal_tax()
print(p1.tax)