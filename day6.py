from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdraw {amount} ETB")
        else:
            print("Not enough money!")

class StatementPrinter:
    def print_statement(self, account: Account):
        print("\n--- ADIS BANK STATEMENT ---")
        print(f"Holder: {account.owner}")
        print(f"Number: {account.account_number}")
        print(f"Balance: {account._balance} ETB")
        print("----------------------------")
if __name__ == "__main__":
    my_account = SavingsAccount("Samuel", "SAV-101", 500.0)
    printer = StatementPrinter()
    my_account.withdraw(150.0)
    printer.print_statement(my_account)