class product():
    def __init__(self, id, name, price, count, The_type) -> None:
        self._id = id
        self.name = name
        self.__price = price
        self.count = count
        self.the_type = The_type

    def info(self):
        return f'the ID is : {self._id}, Name : {self.name}, Price : {self.__price}, How much pieces are in the store {self.count}'
    
    def set_price(self, price):#داخل هذا التابع يمكن اضافة الشيفرات الازمة من اجل حماية من التعديل مثل التسجيل الى الموقع و امتلاك الصلاحيات الازمة
        self.__price = price#يجب استدعاء التابع هذا من اجل تمرير السعر الديد اليه 

    def get_price(self):
        return f'The price is {str(self.__price)} $'

    def discount(self, ratio):
        self.__price = self.__price - self.__price * ratio
        return f'the discount has been made, the price is {self.__price}, with ratio about {ratio}'

iphone13 = product(id=2,name='iphone13',price=999, count=3, The_type='phone')
samsung_s21 =product(id=25,name='samsug', price=1200, count=7, The_type='phone')

iphone13.discount(0.1)
print(f'the new price is:{iphone13.get_price()},and  {iphone13.count} left in the store.')




class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # متغير خاص (Private)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Current balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Current balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance  # الوصول إلى البيانات من خلال دالة عامة

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # الوصول إلى الرصيد باستخدام دالة


class Person:
    def __init__(self, name, age):
        self.name = name           # عام
        self._age = age            # محمي
        self.__ssn = "123-45-6789" # خاص

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, SSN: {self.__ssn}")

person = Person("John", 30)
print(person.name)         # يمكن الوصول
print(person._age)         # يمكن الوصول، لكن من الأفضل عدم التعديل
print(person.__ssn)      # خطأ: لا يمكن الوصول مباشرة
# يمكن الوصول باستخدام الاسم المُعدل (غير مستحسن)
#يمكن تجاوز خاصية الخصوصية في بايثون باستخدام ما يُعرف ب نايم ماندلينج او تشويه الاسماء ، لكن من الأفضل تجنب ذلك للحفاظ على تغليف البيانات.
