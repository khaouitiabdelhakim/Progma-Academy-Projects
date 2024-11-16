# Code By: ABDELHAKIM KHAOUITI
# Date: 12 08 2024
# Place: Rabat
# Org: Progma.ma


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number  # رقم الحساب
        self.account_holder = account_holder  # صاحب الحساب
        self.balance = balance  # الرصيد

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"زيد {amount}. الرصيد الجديد هو {self.balance}")
        else:
            print("المبلغ ديال الإيداع غير صالح")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"سحب {amount}. الرصيد الجديد هو {self.balance}")
        else:
            print("المبلغ ديال السحب غير صالح ولا الرصيد ماكافيش")

    def get_balance(self):
        return self.balance  # رجع الرصيد

    def __str__(self):
        return f"الحساب[{self.account_number}] - صاحب الحساب: {self.account_holder}, الرصيد: {self.balance}"




class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate  # نسبة الفائدة

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"تطبيق الفائدة: {interest}. الرصيد الجديد هو {self.balance}")




class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit  # الحد الأقصى للسحب على المكشوف

    def withdraw(self, amount):
        if (0 < amount <= self.balance) and amount <= self.overdraft_limit:
            self.balance -= amount
            print(f"سحب {amount}. الرصيد الجديد هو {self.balance}")
        else:
            print("المبلغ ديال السحب غير صالح ولا تعدى الحد ديال السحب على المكشوف")









# مثال للاستخدام:
savings_account = SavingsAccount("SA123", "Alice", 1000.0)
current_account = CurrentAccount("CA456", "Bob", 500.0)



print(savings_account)  # طباعة معلومات الحساب الادخاري
savings_account.deposit(500)  # إيداع الفلوس في الحساب الادخاري
savings_account.withdraw(200)  # سحب الفلوس من الحساب الادخاري
savings_account.apply_interest()  # تطبيق الفائدة في الحساب الادخاري
print(savings_account)  # طباعة الرصيد بعد الفائدة

print("--------------------------")


print(current_account)  # طباعة معلومات الحساب الجاري
current_account.deposit(300)  # إيداع الفلوس في الحساب الجاري
current_account.withdraw(1000)  # سحب الفلوس من الحساب الجاري (مع استخدام السحب على المكشوف)
current_account.withdraw(200)  # سحب الفلوس من الحساب الجاري
print(current_account)  # طباعة الرصيد بعد السحب
