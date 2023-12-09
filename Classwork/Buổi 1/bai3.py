class BankAccount:
    def __init__(self, STK, owner, fund):
        self.STK = STK
        self.owner = owner
        self.fund = fund

    def add_fund(self, amount):
        while amount < 0:
            amount = int(input("Invalid! You can't add negative amount.\nHow much do you want to add to your account?: "))
        
        self.fund += amount
        print(f"Balance after adding funds: {self.fund}")

    def withdraw(self, amount):
        while amount > self.fund or amount < 1:
            amount = int(input("Invalid! You can't withdraw more than the amount currently in the fund or a negative amount.\nHow much do you want to withdraw from your account?: "))
        
        self.fund -= amount
        print(f"Balance after withdrawal: {self.fund}")

    def show_information(self):
        print("Here is your account information: ")
        print(f"Account number: {self.STK}\nAccount belongs to: {self.owner}\nAccount remaining funds: {self.fund}")

my_account = BankAccount(STK=7671238762, owner="Chu Minh", fund=2000)

my_account.show_information()

add_amount = int(input("How much do you want to add to your account?: "))
my_account.add_fund(add_amount)

withdraw_amount = int(input("How much do you want to withdraw from your account?: "))
my_account.withdraw(withdraw_amount)

my_account.show_information()
