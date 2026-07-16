from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance 
    @abstractmethod
    def withdraw(self, amount):
        pass

    def statement(self):
        print(f"{self.owner} | Balance: {self._balance} ETB")
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdraw {amount} ETB")
        else:
            print("Not enough money!")

if __name__ == "__main__":
    my_account = SavingsAccount("Samuel", "SAV-101", 500.0)

    my_account.statement()
    my_account.withdraw(200.0)
    my_account.statement()