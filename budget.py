class Category:
	ledger = []
	category = ""

	def __init__(self, category_name):
		self.category = category_name

	def __str__(self):
		title = f"{self.category:*^30}\n"
		items = ""
		total = 0
		for item in self.ledger:
			items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
			total += item['amount']

		output = title + items + "Total: " + str(total)
		return output

	def deposit(self, amount, description = ""):
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description = ""):
		if (self.check_funds(amount)):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		return False

	def get_balance(self):
		money = 0
		for item in self.ledger:
			money += item["amount"]
		return money

	def transfer(self, amount, object):
		if (self.check_funds(amount)):
			self.withdraw(amount, "Transfer to " + object.category)
			object.deposit(amount, "Transfer from " + self.category)
			return True
		return False

	def check_funds(self, amount):
		if (self.get_balance() >= amount):
			return True
		return False

def create_spend_chart(categories):
	return None