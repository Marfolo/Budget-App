class Category:
	ledger = []
	category = ""

	def __init__(self, category_name):
		self.category = category_name

	def deposit(self, amount, description):
		if description is None:
			description == ""
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description):
		#self.ledger.append({"amount": -amount, "description": description})
		if (self.check_funds(amount)):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		return False

	def get_balance(self):
		money = 0
		for item in self.ledger:
			money += item["amount"]
		return money

	def transfer(self, amount, category):
		if (self.check_funds(amount)):
			self.withdraw(amount, "Transfer to " + category.category)
			category.deposit(amount, "Transfer from " + self.category)
			return True
		return False

	def check_funds(self, amount):
		if (self.get_balance() >= amount):
			return True
		return False

def create_spend_chart(categories):
	return None