class BankAccount:
  def __init__(self, interest_rates=0.01, balance=0):
    self.interest_rates = interest_rates
    self.balance = balance

  # @classmethod
  def deposit(self, deposit=0):
    self.balance += deposit
    return self

  # @classmethod
  def withdraw(self, withdraw=0):
    if self.balance < withdraw:
      print(f"insufficient funds: Charging a $5 fee")
      self.balance -= 5
    else:
      self.balance -= withdraw
    return self

  # @classmethod
  def display_account_info(self):
    print(f"Balance: {self.balance}")
    return self
  
  # @classmethod
  def yield_interest(self):
    return self

panther = BankAccount(5, 1000)
credit = BankAccount(7, 1000)

panther.deposit(100).deposit(1000).deposit(500).withdraw(100).display_account_info()
credit.deposit(10).deposit(10).withdraw(100).withdraw(50).withdraw(500).withdraw(500).display_account_info()

