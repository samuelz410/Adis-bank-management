class Account:
    def __init__(self, owner, account_number, initial_balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount} ETB")
        else:
            print("Invalid deposit amount!")

    # 3. Withdraw Method
    def withdraw(self, amount):
        # Validation lives inside: check if we have enough money and amount is positive
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount} ETB")
        else:
            print("Declined: Insufficient funds or invalid amount!")
    def statement(self):
        print("--- Account Statement ---")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance} ETB")
        print("-------------------------")


