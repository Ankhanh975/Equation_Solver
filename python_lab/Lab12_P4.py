# D. Bank Account Management
# Task is to create a simple bank account management system using object-oriented programming. 
# Implement two classes: Account, CheckingAccount. 
# Each class should perform different tasks related to handling bank accounts.

# Account (Base Class):
# Attributes (private): _account_id: Stores the unique identifier for the account. 
# __balance: Stores the account's balance.
# Methods: 
# deposit(amount): Deposits money into the account. 
# withdraw(amount): Withdraws money from the account (if sufficient balance).
# Getter Methods: get_balance(): Returns the current balance.
# Setter Methods: set_balance(new_balance): Updates the balance of the account.
class Account:
    def __init__(self, account_id, initial_balance=0):
        self._account_id = account_id
        self.__balance = initial_balance
    
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposit successful to account {self._account_id}. Updated balance: {self.__balance}"
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Withdrawal successful from account {self._account_id}. Updated balance: {self.__balance}"
    
    def get_balance(self):
        return int(self.__balance)
    
    def set_balance(self, new_balance):
        self.__balance = new_balance

# CheckingAccount (Derived Class):
# Attributes: __fee: Represents the fee charged for withdrawals.
class CheckingAccount(Account):
    def __init__(self, account_id, initial_balance=0, fee=5):
        super().__init__(account_id, initial_balance)
        self.__fee = fee

    def withdraw(self, amount):
        # Methods: Overrides withdraw(amount):
        # If the withdrawal is successful, return: Withdrawal successful from account <_account_id> 
        # (including fee of <__fee>). Updated balance: <__balance>.
        # If the amount is not sufficient, return: Invalid withdrawal amount.
        # Otherwise, return: Insufficient balance.

        total_withdrawal = amount + self.__fee
        if total_withdrawal > self.get_balance():
            return "Insufficient balance."
        
        self.set_balance(self.get_balance() - total_withdrawal) 
        return f"Withdrawal successful from account {self._account_id} (including fee of {self.__fee}). Updated balance: {self.get_balance()}"
    
    # Overrides deposit(amount):
    # If the account exists, return: Deposit successful to account <_account_id>. 
    # Updated balance: <__balance>.
    # Deducts the fee along with the withdrawal amount when the balance is sufficient.
    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount) 
        # if self.get_balance() > self.__fee:
            # self.set_balance(self.get_balance() - self.__fee) 
        return f"Deposit successful to account {self._account_id}. Updated balance: {self.get_balance()}"
    
    # Getter and Setter for Fee: get_fee(): Returns the withdrawal fee. set_fee(new_fee): 
    # Updates the withdrawal fee.
    def get_fee(self):
        return self.__fee
    
    def set_fee(self, new_fee):
        self.__fee = new_fee

if __name__ == "__main__":
    # Input
    # The input consists of multiple lines:

    # The first line contains an integer n ((1 <= n <= 10)), representing the number of commands.
    # The following n lines contain commands in the following format:
    # account_id deposit amount: 
    # Deposits the specified amount into the account with the given account ID.
    # account_id amount: 
    # Creates an account with the given account ID and an initial balance.
    # account_id withdraw amount: 
    # Withdraws the specified amount from the account with the given account ID.
    # The program should check if the account exists before performing operations.
    accounts = {}
    n = int(input().strip())
    parts = []
    for _ in range(n):
        parts.append(input().strip().split())
        
    # Output
    for i in range(n):
        part = parts[i]
        account_id = int(part[0])
        
        if len(part) == 2:
            # Create account or deposit
            # For each command, output the result:

            # If an account doesn't exist, print "Account does not exist."
            # For deposits and withdrawals, print the success message along with the updated balance inside the withdraw and deposit functions after execution.
            # If the withdrawal cannot be completed due to insufficient funds, print "Insufficient balance."

            if part[1].isdigit():
                accounts[account_id] = CheckingAccount(account_id, initial_balance=float(part[1]))
                print(f"Account {account_id} created with balance: {int(accounts[account_id].get_balance())}")
            else:
                # Deposit command
                if account_id not in accounts:
                    print("Account does not exist.")
                else:
                    amount = float(part[2])
                    print(accounts[account_id].deposit(amount))
        
        elif len(part) == 3:
            if "withdraw" in part: 
                # Withdraw command
                if account_id not in accounts:
                    print("Account does not exist.")
                else:
                    amount = float(part[2])
                    print(accounts[account_id].withdraw(amount))
            elif "deposit" in part:
                # Deposit command
                if account_id not in accounts:
                    print("Account does not exist.")
                else:
                    amount = float(part[2])
                    print(accounts[account_id].deposit(amount))


