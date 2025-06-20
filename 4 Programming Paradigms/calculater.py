# بوابة AND
def logical_and(a, b):
    return a * b

# بوابة OR
def logical_or(a, b):
    return a + b - (a * b)

# بوابة NOT
def logical_not(a):
    return 1 - a

# عملية الجمع
def add(a, b):
    return a + b

# عملية الطرح
def subtract(a, b):
    return a + logical_not(b) * -1

# عملية الضرب باستخدام بوابة AND
def multiply(a, b):
    result = 0
    for _ in range(b):
        result = add(result, a)
    return result

# عملية القسمة (تقريبية)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    result = 0
    while a >= b:
        a = subtract(a, b)
        result = add(result, 1)
    return result

# واجهة المستخدم
def calculator():
    print("Welcome to the Logical Calculator!")
    print("Choose an operation:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    choice = int(input("Enter your choice: "))

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if choice == 1:
        print(f"Result: {add(a, b)}")
    elif choice == 2:
        print(f"Result: {subtract(a, b)}")
    elif choice == 3:
        print(f"Result: {multiply(a, b)}")
    elif choice == 4:
        print(f"Result: {divide(a, b)}")
    else:
        print("Invalid choice!")

calculator()
