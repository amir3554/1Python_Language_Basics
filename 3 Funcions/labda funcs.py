# دالة lambda لإضافة رقمين
add = lambda x, y: x + y

# استخدام الدالة
result = add(5, 3)
print(result)  # 8


# استخدام lambda داخل الدالة sorted
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers, key=lambda x: -x)  # ترتيب تنازلي
print(sorted_numbers)  # [9, 5, 4, 3, 1, 1]


# رفع الأرقام إلى القوة 2 باستخدام map
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]

# تصفية الأرقام الزوجية باستخدام filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4]


# دالة lambda لحساب مساحة مستطيل
area = lambda length, width: length * width
print(area(5, 3))  # 15


Ids = ['id22', 'id100', 'id3', 'id300', 'id82']

Ids.sort(key= lambda x : int(x[2:]))

print(Ids)





