def greet(name, age, nick_name = '', b_date= "0000/00/00" ):
    print(f"Welcome {name}, Age:{age} years old, Surname: {nick_name}, Your birth day will be {b_date}")
    

def greet_with_kwargs(**kwargs):
    for kwarg in kwargs:
        print(f'========{kwargs.get(kwarg)}========')
    

def faundations( number1=0, number2=0):
    print(f"number 1: {number1} ^ Number 2: {number2}, the answer is {number1 ** number2}")


def is_even(*args):
    for arg in args:
        if arg % 2 == 0:
            print('the number is even. True ')
        elif arg % 2 !=0:
            print('The number is odd. False ')
        else:
            return


greet(name='amir', age= 18, nick_name="Amr", b_date="2006/4/9")
greet_with_kwargs(name='saeed', age= 25, job='IT')
faundations(4, 8)
print('==============')
is_even(28286, 7 , 4 , 5)


x = 100

def printx():
    x = 200
    print(x)

printx()
print(x)

