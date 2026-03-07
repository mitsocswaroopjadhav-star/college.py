import datetime
import random
import sys

class BankAccount:
    def __init__(self, owner_name, account_number, initial_balance=0.0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = initial_balance
        self.bank_name = "MY BANK"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.generate_receipt("DEPOSITE", amount)
        else:
            print("\n[!] Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"\n[!] Transaction Declined: Insufficient funds. Balance is ${self.balance:,.2f}")
        elif amount <= 0:
            print("\n[!] Error: Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.generate_receipt("WITHDRAWAL", amount)

    def generate_receipt(self, transaction_type, amount):
        # Get current date and time
        now = datetime.datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # Generate a fake transaction ID
        trans_id = f"TXN-{random.randint(10000, 99999)}"
        
        # Mask the account number (show only last 4 digits)
        masked_acc = f"*****{str(self.account_number)[-4:]}"

        # Print the receipt
        print("\n" + "="*40)
        print(f"{self.bank_name:^40}")
        print("="*40)
        print(f"Date/Time:      {date_time_str}")
        print(f"Transaction ID: {trans_id}")
        print(f"Customer:       {self.owner_name}")
        print(f"Account No:     {masked_acc}")
        print("-" * 40)
        print(f"Type:           {transaction_type}")
        print(f"Amount:         ${amount:,.2f}")
        print("-" * 40)
        print(f"TOTAL BALANCE:  ${self.balance:,.2f}")
        print("=" * 40)
        print(f"{'Thank you for banking with us!':^40}")
        print("=" * 40 + "\n")

# --- Main Program Execution ---
def main():
    # Initialize a dummy account
    print("--- Welcome to My Bank ---")
    name = input("Enter Account Holder Name: ")
    acc_num = random.randint(1000000000, 9999999999) # Simulating a fixed account number
    print("Account Number:", acc_num)
    # Create account object with $1000 starting balance
    my_account = BankAccount(name, acc_num, 1000.00)

    while True:
        # print(f"Current Balance: ${my_account.balance:,.2f}")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        try:
            if choice == '1':
                amt = float(input("Enter amount to deposit: $"))
                my_account.deposit(amt)
            elif choice == '2':
                amt = float(input("Enter amount to withdraw: $"))
                my_account.withdraw(amt)
            elif choice == '3':
                print(f"\n[=] Available Balance: ${my_account.balance:,.2f}\n")
            elif choice == '4':
                print("Exiting system. Have a nice day!")
                sys.exit()
            else:
                print("\n[!] Invalid option. Please try again.\n")
        except ValueError:
            print("\n[!] Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    main()