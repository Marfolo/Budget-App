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
		if amount > ledger.


def create_spend_chart(categories):