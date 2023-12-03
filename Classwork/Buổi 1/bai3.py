class BankAccount:
    def __init__(self, STK, owner, fund):
        self.STK = STK
        self.owner = owner
        self.fund = fund

    def add_fund(self):
        print(f"balance before adding fund: {self.fund}")
        value = int(input("How much you wanna add to your account?: "))
        while value < 0:
            value = int(input("Invalid!, you cant add negative to the account!\nHow much you wanna add to your account?: "))

        self.fund += value
        print(f"balance after adding fund: {self.fund}")

    def withdraw(self):
        print(f"balance before withdraw: {self.fund}")
        value = int(input("How much you wanna withdraw from your account?: "))
        while value > self.fund or value < 1:
            value = int(input("Invalid!, you cant withdraw more than or negative the amount currently in the fund.\nHow much you wanna withdraw from your account?: "))
        self.fund -= value
        print(f"balance after withdraw: {self.fund}")

    def show_information(self):
        print("Here is your account information: ")
        print(f"Account number: {self.STK}\nAccount belong to: {self.owner}\nAccount remaining funds: {self.fund}")

my_account = BankAccount(STK=7671238762, owner="Chu Minh", fund=2000)

my_account.show_information()

my_account.add_fund()
my_account.withdraw()
my_account.show_information()
