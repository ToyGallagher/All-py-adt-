'''
#1
class BankAccount:
    def __init__(self,accountID="",balance=0.0):
        self.accountID = accountID
        self.balance = balance
    def __str__(self):
        return f"ID: {self.accountID}, Balance: {self.balance:.2f}"
    def set_account_ID(self,newID):
        self.accountID = newID
    def set_balance(self, new_balance):
        self.balance = new_balance
    def deposit(self, amount):
        self.balance = self.balance+amount
    def withdrawal(self, amount):
        self.balance = self.balance-amount
    def get_account_ID(self):
        return self.accountID
    def get_balance(self):
        return self.balance

account = BankAccount("1001",500)


while True:
    choice = int(input("Deposit (1), Withdrawal (2), Update (3), or Exit (0): "))
    if choice == 0:
        break
    elif choice == 1:
        amount = float(input("Enter your deposit amount: "))
        account .deposit(amount)
        print(account)
    elif choice == 2:
        amount = float(input("Enter your withdrawal amount: "))
        account .withdrawal(amount)
        print(account)
    else:
        amount = float(input("Enter your update amount: "))
        account .set_balance(amount)
        print(account)

print(account.get_account_ID())
print(account.get_balance())
account.set_balance(5000)
print(account.get_balance())

amount = float(input("Enter your deposit amount: "))
account.deposit(amount)
print(amount)

amount = float(input("Enter your withdrawal amount: "))
account.withdrawal(amount)
print(account)
'''

#2

class Radio:
    def __init__(self,mode = "FM",frequency = 87.5):
        self.__mode = mode
        self.__frequency = frequency
    def get_mode(self):
        return self.__mode
    def get_frequency(self):
        return self.__frequency
    def set_mode(self,mode):
        self.__mode = mode
        self.__frequency = 150
        if mode=="FM":
            self.__frequency == 87.5
    def set_frequency(self,frequency):
        if self.__mode == "FM" and 87.5<=frequency<=108:
            self.__frequency = frequency
        elif 150<=frequency<=280:
            self.__frequency = frequency

#3



'''
#6
import math
class Cylinder:
    def __init__(self,radius=4.123,height=2.000):
        self.radius = radius
        self.height = height
    def __str__(self):
        return f"Radius: {self.radius:.3f}, Height: {self.height:.3f}"
    def set_radius(new_radius):
        self.radius = new_radius
    def set_height(new_height):
        self.height = new_height
    def get_radius(self):
        return self.radius
    def get_height(self):
        return self.height
    def get_base_area(self):
        return self.radius*math.pi
    def get_volume(self):
        return self.radius*math.pi*self.height
'''

