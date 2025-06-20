def check_number():
    while True:
        user_input = input("Enter the number , the number from 0 to 100. ")

        # التحقق من أن الإدخال ليس فارغًا
        if not user_input.strip():
            print("You haven't entered a number. ")
            continue

        # التحقق من أن الإدخال عبارة عن رقم صالح
        if not user_input.isdigit():
            print("Please enter a valid number. ")
            continue

        # تحويل الإدخال إلى عدد والتحقق من النطاق
        number = int(user_input)
        if 0 <= number <= 100:
            print(f"The {number} is a valid number! ")
            return number
        else:
            print("The number is out of range , Please enter a number bitween 0 and 100.")

#check_number()

try:
    x = int(input("أدخل رقمًا: "))
    result = 10 / x
    print("النتيجة:", result)
except ValueError:
    print("يرجى إدخال رقم صحيح!")
except ZeroDivisionError:
    print("لا يمكن القسمة على صفر!")

#try:
        # الكود الذي قد يسبب استثناء

#except نوع_الاستثناء:

        # ماذا تفعل إذا حدث الاستثناء




#التمرين 1: معالجة خطأ القسمة على صفر
#while True:
try:  
    x2 = int(((input(((("Please enter a number. ")))))))
    resault = 100/x2
    print(f"The resault : {resault}")
except ZeroDivisionError:
    print("It cant be divided by zero.")
    #continue
except ValueError:
    print("Please enter a valid number. ")
        #continue

#التمرين 2: الوصول إلى عنصر من قائمة
numbers = [10, 20, 30, 40, 50]
try:
    num = int(input("Enter an index : "))
    print(f"The number from numbers with index {num}, is {numbers[num]}")
except (ValueError, IndexError) as e:
    print("Please enter a valid number.", e)

#التمرين 3: التحقق من إدخال المستخدم


positive_input = int(input("Please enter a positive number only."))
print(f"This is a valid number : ) . {positive_input}")
if positive_input < 0:
    raise ValueError("Enter a postive number only bruh.")

#التمرين 4: معالجة خطأ فتح الملفات
try: 
    file =open("data.txt", 'r') 
except FileNotFoundError:
    print("this file does not exist.")
finally:
    file.close()

#التمرين 5: استثناءات متعددة
from math import sqrt
try:
    SQRT_num = int(input("please enter a number to get the square root for it."))
    resault = sqrt(SQRT_num)
    print(resault)
except (ValueError, TypeError) as e:
    print("Pleas enter a valid number to get the sqrt for it.\n ",e)


#التمرين 6: حساب المعدل

from functools import reduce
num_list = []
try:
    user_input= input("Please enter numbers to get the avarage, put space between every number. ")
    for n in user_input:
        if n ==' ':
            continue
        else:
            num_list.append(int(n))
    the_sum = int(reduce(lambda x, y : x + y, num_list))
    avarage = the_sum / len(num_list)
    print(avarage)
        
except (ValueError, TypeError, ZeroDivisionError, SyntaxError) as e:
    print("Please enter a valid number...", e)
else:
    print(f"Every thing went okey, no Errors, this is 'else SoftWare Block' and it will be implemented if there is no errors ,and the avagage of the list that you entered which is {num_list} ,and has a {len(num_list)} of elements is {avarage}. ")
finally:
    print("Every thing is done ,This is the 'finally SoftWare Block' ,and it will be implemented by the interpreter. ")

class TooYoungError(Exception):
    def __init__(self,massage) -> None:
        self.MASSAGE = massage

    def __str__(self):
        return self.MASSAGE
         

class TooOldError(Exception):
    def __str__(self) -> str:
        return 'You are too old.'

'''
#age = int(input("enter you age: "))
#if age > 65: raise TooOldError
#if age < 16: raise TooYoungErrortry:
'''
try:
    age = int(input("enter you age: "))      
    if age in range(16,66):
        print("You can enter.")
    elif age < 16:
        raise TooYoungError(f"You are {age} years old, too young. ")
    else:
        raise TooOldError
except TooOldError as e:
    print(e)
except TooYoungError as e:
    print(e)
except ValueError as e:
    print("enter a correct age")



