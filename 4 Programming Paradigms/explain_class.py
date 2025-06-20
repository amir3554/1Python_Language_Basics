#انا ادرس لغة بايثون حاليا و اريد شرحا مفصلا عن الأصناف والكائنات والخصائص والتوابع و ليس مقالا عاما لو سمحت

class Car:
    pass  # كلمة pass تعني أن الصنف فارغ حالياً



my_car = Car()  # إنشاء كائن من الصنف Car
print(my_car)   # يعرض موقع الكائن في الذاكرة



class Car2:
    def __init__(self, brand, color):  # المُهيئ Constructor
        self.brand = brand  # خاصية العلامة التجارية
        self.color = color  # خاصية اللون

my_car2 = Car2("Toyota", "Red")  # إنشاء كائن
print(my_car2.brand)  # طباعة العلامة التجارية
print(my_car2.color)  # طباعة اللون



class Car3:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):  # تعريف تابع
        print(f"The {self.color} {self.brand} is driving.")

my_car3 = Car3("Toyota", "Red")
my_car3.drive()  # استدعاء التابع

#The Red Toyota is driving.



class Car4:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def repaint(self, new_color):
        self.color = new_color  # تعديل الخاصية
        print(f"The car has been repainted to {self.color}.")


my_car4 = Car4("Toyota", "Red")
my_car4.repaint("Blue")  # إعادة طلاء السيارة
#The car has been repainted to Blue.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, and my grade is {self.grade}.")

student1 = Student("Alice", 14, "A")
student1.introduce()

#My name is Alice, I am 14 years old, and my grade is A.

class Car5:
    def __init__(self, brand, color):
        self.brand = brand  # خاصية عامة

my_car5 = Car5("Toyota", "Red")
print(my_car5.brand)  # الوصول إلى الخاصية مباشرة

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # خاصية خاصة

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # طريقة للوصول إلى الخاصية الخاصة

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

class product():
    def __init__(self, id, name, price, count, The_type) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.count = count
        self.the_type = The_type

    def info(self):
        return f'the ID is : {self.id}, Name : {self.name}, Price : {self.price}, How much pieces are in the store {self.count}'
    
    def discount(self, ratio):
        self.price = self.price - self.price * ratio
        return f'the discount has been made, the price is {self.price}, with ratio about {ratio}'

iphone13 = product(id=2,name='iphone13',price=999, count=3, The_type='phone')
samsung_s21 =product(id=25,name='samsug', price=1200, count=7, The_type='phone')

iphone13.discount(0.1)
print(f'the new price is:{iphone13.price},and  {iphone13.count} left in the store.')

