class Checkbill:
	def __init__(self, checkID, amount, tip, isPaid):
		self.checkID = checkID
		self.amount = amount
		self.tip = tip
		self.isPaid = isPaid

	def create_bill(self):
		pass

class Payment:
	def __init__(self, PaymentID, amount, creationData):
		self.PaymentID = PaymentID
		self.amount = amount
		self.creationData = creationData
	
	def intiate_transaction(self):
		pass

class CreditTransaction(Payment):
	pass

class CheckTransaction(Payment):
	pass

class CashTransaction(Payment):
	pass