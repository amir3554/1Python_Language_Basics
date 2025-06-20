def add(x, y):
    return x + y


def double(x):
    return x * 2

def square(x):
    return x ** 2

result = square(double(3))  # 36


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]


numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16]


from functools import reduce
numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # 10
