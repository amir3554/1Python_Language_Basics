# قائمة عادية
my_list = [1, 2, 3, 4]

# إنشاء مكرر
my_iterator = iter(my_list)

# الحصول على العناصر باستخدام المكرر
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
print(next(my_iterator))  # 4

# إذا حاولنا استدعاء next مرة أخرى، ستظهر StopIteration


class MyIterator:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# استخدام المكرر
my_iter = MyIterator(5)
for num in my_iter:
    print(num)  # يطبع الأرقام من 1 إلى 5



def my_generator():
    yield 1
    yield 2
    yield 3

# استخدام المولد
gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# إذا حاولنا استدعاء next مرة أخرى، ستظهر StopIteration


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # يطبع 5, 4, 3, 2, 1


def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

# استخدام المولد
gen = infinite_numbers()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

#حاصل جمع مربعات الاعداد الفردية بالستخدام المولدات 
print("__________________________")

def sumquareodd(num):
    num = int(num)
    num_list =[]
    x = 1
    while x <= num:
        num_list.append(x)
        x += 2
    num_list_square =[square **2 for square in num_list ]
    sum = 0
    for j in num_list_square:
        sum = j + sum
    return print(sum)
    
sumquareodd(10)

def odd_numbers(number):
    for num in range(1 , number , 2):
        yield num


def square(nums):
    for num in nums:
        yield num ** 2

print(sum(square(odd_numbers(10))))


