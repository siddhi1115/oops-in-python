class Bank_account:
  def __init__(self,name,account_no,balance):
    self.name = name
    self.account_no = account_no
    self.balance = balance

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
    else:
      print("Insufficient balance")

b1 = Bank_account("Siddhi", 123456789, 50000)
print("Name:", b1.name)
print("Account number:", b1.account_no)
print("Account balance:", b1.balance)

amount = float(input("Enter the amount to withdraw: "))
b1.withdraw(amount)
print("Updated balance:", b1.balance)