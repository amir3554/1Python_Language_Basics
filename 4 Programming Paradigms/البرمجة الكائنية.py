# تعريف الصنف
class Car:
    def __init__(self, brand, color):  # المُهيئ (Constructor)
        self.brand = brand  # خاصية العلامة التجارية
        self.color = color  # خاصية اللون

    def drive(self):  # أسلوب القيادة
        print(f"The {self.color} {self.brand} is driving.")

# إنشاء كائن
my_car = Car("Toyota", "red")
my_car.drive()
# Output: The red Toyota is driving.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # عام
        self.__balance = balance  # خاص (Private)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

# إنشاء حساب
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)        # Output: Insufficient funds!


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting.")

# الوراثة من Vehicle
class Car2(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving.")

# إنشاء كائن
my_car = Car2("BMW")
my_car.start()  # Output: BMW is starting.
my_car.drive()  # Output: BMW is driving.


class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
# Output:
# Woof
# Meow









