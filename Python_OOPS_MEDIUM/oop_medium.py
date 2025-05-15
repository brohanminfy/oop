class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type

class BankAccount:
    def __init__(self, account_number, balance):
        super().__setattr__('_BankAccount__account_number', account_number)
        super().__setattr__('_BankAccount__balance', balance)

    def deposit(self, amount):
        if amount > 0:
            object.__setattr__(self, '_BankAccount__balance', self.__balance + amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            object.__setattr__(self, '_BankAccount__balance', self.__balance - amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def __setattr__(self, name, value):
        # Prevent external direct modification of __balance
        if name in ('__balance', '_BankAccount__balance'):
            raise AttributeError("Direct modification of private balance is not allowed")
        super().__setattr__(name, value)



# Medium Assignment 1

car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)   # Output: Toyota
print(car.doors)  # Output: 4




# Medium Assignment 2
account = BankAccount("123456", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(200)
print(account.get_balance())  # Output: 1300
print(account.get_account_number())  # Output: 123456


try:
    account.__balance = 2000  
    print(account.__balance)  
except AttributeError:
    print("Cannot directly access private attribute")

print(account.get_balance())  # Output: 1300