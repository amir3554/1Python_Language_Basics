from abc import ABC, abstractmethod

# الفئة المجردة: شكل
class shape(ABC):
    @abstractmethod
    def area_calculation(self):
        """طريقة لحساب المساحة"""
        pass

    @abstractmethod
    def circumference_calculation(self):
        """طريقة لحساب المحيط"""
        pass

# الفئة الفرعية: دائرة
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area_calculation(self):
        return 3.14 * self.radius ** 2

    def circumference_calculation(self):
        return 2 * 3.14 * self.radius

# الفئة الفرعية: مستطيل
class Rectangle(shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area_calculation(self):
        return self.height * self.width

    def circumference_calculation(self):
        return 2 * (self.height + self.width)

# الفئة الفرعية: مثلث
class Triangle(shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area_calculation(self):
        return 0.5 * self.base * self.height

    def circumference_calculation(self):
        return self.side1 + self.side2 + self.side3

# استخدام الفئات
def run():
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(6, 4, 3, 4, 5)
    ]

    for shape in shapes:
        print(f"الشكل: {shape.__class__.__name__}")
        print(f"المساحة: {shape.area_calculation()}")
        print(f"المحيط: {shape.circumference_calculation()}")
        print("-" * 30)

# تشغيل البرنامج
run()
