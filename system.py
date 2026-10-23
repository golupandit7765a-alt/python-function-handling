class BankAccount:
    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.__balance = balance  # Encapsulation
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"{amount} Deposited. New Balance: {self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        try:
            if amount > self.__balance:
                raise ValueError("Insufficient Balance")
            self.__balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print(f"{amount} Withdrawn. New Balance: {self.__balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def get_balance(self):
        return self.__balance

    def show_history(self):
        print(f"Transaction history for {self.name}:")
        for t in self.transactions:
            print("-", t)

# Inheritance Example
class SavingsAccount(BankAccount):
    def __init__(self, account_no, name, balance=0, interest_rate=0.05):
        super().__init__(account_no, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest Added: {interest}")

# Demo
if __name__ == "__main__":
    acc1 = SavingsAccount("101", "Golu Pandit", 1000)
    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.add_interest()
    acc1.show_history()
