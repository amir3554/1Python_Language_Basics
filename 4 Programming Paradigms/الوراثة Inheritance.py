class Animal:  # الفئة الرئيسية
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# الفئة الفرعية
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# إنشاء الكائنات
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!



class Vehicle:
    def move(self):
        return "The vehicle moves"

class Car(Vehicle):
    def move(self):
        return "The car drives on the road"



class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def roll(self):
        return "Wheels are rolling"

class Car2(Engine, Wheels):
    pass

my_car = Car2()
print(my_car.start())  # Engine started
print(my_car.roll())   # Wheels are rolling



class Animal2:
    def eat(self):
        return "Eating"

class Mammal(Animal2):
    def walk(self):
        return "Walking"

class Dog2(Mammal):
    def bark(self):
        return "Barking"



class Shape:
    def draw(self):
        return "Drawing shape"

class Circle(Shape):
    def draw(self):
        return "Drawing circle"

class Square(Shape):
    def draw(self):
        return "Drawing square"



class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

child = Child()
print(child.greet())  # Hello from Child



class Parent2:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"

class Child2(Parent2):
    def __init__(self, name, age):
        super().__init__(name)  # استدعاء المُنشئ من الفئة الرئيسية
        self.age = age

    def greet(self):
        return f"{super().greet()} and I am {self.age} years old"

child = Child2("John", 10)
print(child.greet())  # Hello, I am John and I am 10 years old



