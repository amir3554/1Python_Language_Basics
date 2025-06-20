def get_number(prompt):
    while True:
        try:
            # طلب إدخال رقم من المستخدم
            return float(input(prompt))
        except ValueError:
            # عرض رسالة خطأ مخصصة في حال إدخال حرف بدلاً من رقم
            print("خطأ: يرجى إدخال رقم صالح!")

def calculator():
    print("مرحبًا بك في الآلة الحاسبة!")
    print("اختر العملية:")
    print("1: جمع")
    print("2: طرح")
    print("3: ضرب")
    print("4: قسمة")

    while True:
        try:
            # طلب إدخال خيار العملية
            choice = int(input("أدخل رقم العملية (1-4): "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError("الخيار غير صحيح")
            break
        except ValueError:
            print("خطأ: يرجى إدخال رقم بين 1 و 4!")

    # طلب إدخال الرقمين
    num1 = get_number("أدخل الرقم الأول: ")
    num2 = get_number("أدخل الرقم الثاني: ")

    # تنفيذ العملية بناءً على الخيار
    if choice == 1:
        print(f"النتيجة: {num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"النتيجة: {num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"النتيجة: {num1} x {num2} = {num1 * num2}")
    elif choice == 4:
        if num2 == 0:
            print("خطأ: لا يمكن القسمة على الصفر!")
        else:
            print(f"النتيجة: {num1} ÷ {num2} = {num1 / num2}")

# تشغيل الآلة الحاسبة
calculator()


def is_prime(n , i =2):
    if n <= 2:
        if n ==2:
            return True
        else:
            return False
    if n % i == 0:
        return False
    if (i * i > n ):
        return True
    return is_prime(n , i + 1)

is_prime(17)

