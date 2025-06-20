class Cat:
    def sound(self):
        return "meow"

class Dog:
    def sound(self):
        return "bark"

class Duck:
    def sound(self):
        return "wack"

# دالة تستخدم تعدد الأشكال
def make_sound(animal):
    print(animal.sound())

# استخدام الدالة مع كائنات مختلفة
animal = [Cat(), Dog(), Duck()]

for animal in animal:
    make_sound(animal)


##########################


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # تحميل العامل +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # تمثيل الكائن كنص
    def __repr__(self):
        return f"({self.x}, {self.y})"

# إنشاء كائنات من الفئة point
point1 = Point(2, 3)
point2 = Point(4, 5)

# جمع النقاط باستخدام +
point3 = point1 + point2

print("point1:", point1)
print("point2:", point2)
print("point3 (ناتج الجمع):", point3)


##########################


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point4 = Point2(2, 3)
point5 = Point2(2, 3)
point6 = Point2(4, 5)

print(point4 == point5)  # True
print(point4 == point6)  # False


##########################


class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point3(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

point7 = Point3(5, 7)
point8 = Point3(2, 3)

point9 = point7 - point8
print(point9)  # (3, 4)


class Point4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, num):
        return Point4(self.x * num, self.y * num)

    def __repr__(self):
        return f"({self.x}, {self.y})"

point10 = Point4(3, 4)
point11 = point10 * 2
print(point11)  # (6, 8)


##########################


def check_number():
    while True:
        user_input = input("أدخل رقمًا بين 0 و 100: ")

        # التحقق من أن الإدخال ليس فارغًا
        if not user_input.strip():
            print("الإدخال فارغ. يرجى إدخال رقم صالح.")
            continue

        # التحقق من أن الإدخال عبارة عن رقم صالح
        if not user_input.isdigit():
            print("الإدخال ليس رقمًا. يرجى إدخال رقم صحيح.")
            continue

        # تحويل الإدخال إلى عدد والتحقق من النطاق
        number = int(user_input)
        if 0 <= number <= 100:
            print(f"الرقم {number} صالح!")
            return number
        else:
            print("الرقم خارج النطاق. يرجى إدخال رقم بين 0 و 100.")

# استدعاء الدالة
check_number()


##########################


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# استخدام الكلاس
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # النتيجة: Vector(6, 8)

print(dir(int))


##########################


class Point5():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point5(self.x + other.x , self.y + other.y , self.z + other.z)

    def __str__(self):
        return f'x : {self.x}, y : {self.y}, z : {self.z}'

    def __lt__(self, other):
        first =((self.x **2) + (self.y **2) + (self.z ** 2))
        second = ((other.x **2) + (other.y **2) + (other.z ** 2))
        if  first < second:
            return True
        elif first > second:
            return False  
        else:
            return(f"The {self} Point = The {other} Point") 

    def __gt__(self, other):
        first =((self.x **2) + (self.y **2) + (self.z ** 2))
        second = ((other.x **2) + (other.y **2) + (other.z ** 2))
        if  first > second:
            return True
        elif first < second:
            return False  
        else:
            return(f"The {self} Point = The {other} Point")


point12 = Point5(4, 5, -11)
point13 = Point5(1, -5, 7)
point14 = Point5(-4, 5, 11)
print("---------------")
print(point12 + point13)
print("---------------")
print(point12 > point13)
print("---------------")
print(point12 < point13)
print("---------------")
print(point12 > point14)
print("---------------")

#يمكن حساب طول النقطة بايجاد حاصل جمع مربعات احداثياتها ويجب ان نعمل مقارنة بين النقاط

    


