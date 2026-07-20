from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, owner, account_number, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
        self.history = []  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.history.append(("deposit", amount))  
            print(f" Deposited {amount} ETB")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.history.append(("withdraw", amount))  
            print(f" Withdrew {amount} ETB")
            return True
        print(" Transaction declined!")
        return False

    def undo_last(self):
        """Pops the most recent transaction (LIFO) and reverses its effect."""
        if not self.history:
            print(" No transactions to undo!")
            return

        action, amount = self.history.pop() 
        if action == "deposit":
            self._balance -= amount
            print(f" Undid deposit of {amount} ETB")
        elif action == "withdraw":
            self._balance += amount
            print(f" Undid withdrawal of {amount} ETB")

class SavingsAccount(Account):
    pass
class AccountRegistry:
    def __init__(self):
        self.by_number = {}  
        self.order = []      

    def add(self, acc):
        """Adds an account to the registry."""
        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)

    def find(self, number):
        """O(1) lookup by account number."""
        return self.by_number.get(number)

    def list_all(self):
        """Returns accounts in insertion order."""
        return [self.by_number[num] for num in self.order]
if __name__ == "__main__":
    registry = AccountRegistry()

    acc1 = SavingsAccount("Samuel", "SAV-101", 1000.0)
    registry.add(acc1)

    found = registry.find("SAV-101")
    print(f"Found Account for: {found.owner}")
    found.deposit(200.0)   
    found.withdraw(50.0)   
    print(f"Current Balance: {found._balance} ETB")

    found.undo_last()
    print(f"Balance after undo: {found._balance} ETB")  