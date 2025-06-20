temps = [('nablus' , 19), ('al quds' , 21), ('bagdad' , 25), ('valencia' , 16)]
# f = 1.8 x C + 32
'''
def C_To_F(item):
    return item[0], 1.8 * item[1] + 32

f_temps = list(map(C_To_F, temps))

temps = []

for item in temps:
    f = item[1] * 1.8 + 32
    temps.appened((item[0], f))

'''
f_temps = list(map(lambda item :(item[0], (item[1] * 1.8 + 32)), temps))

print(f_temps)



languages = [('C', 1972), ('C++', 1985), ('Java', 1985), ('Javascript', 1995), ('PHP', 1994), ('Python', 1991) ]

old_languages = list(filter(lambda item :(item[1]  < 1990 ), languages))

print(old_languages)
print(languages)

'''
old_languages = [(name, year) for name, year in languages if year < 1990]
print(old_languages)
# Output: [('C', 1972), ('Fortran', 1957)]

languages = [("Python", 1991), ("C", 1972), ("Java", 1995), ("Fortran", 1957)]
# تصفية اللغات التي ظهرت قبل 1990
old_languages = list(filter(lambda item: item[1] < 1990, languages))
print(old_languages)
# Output: [('C', 1972), ('Fortran', 1957)]
'''

def find(iterable, text):
    def finder(insider_tuple):
        for i in insider_tuple:
            if str(i).startswith(text):
                return True
            return False
    return list(filter(finder, iterable))

resaults = find(languages, 'J')
print(resaults)

from functools import reduce

# Find the product of all numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

numbers2 = [1, 2, 3, 4, 5, 6]
sums = reduce(lambda x, y : x + y, numbers2)
print(sums)

numbers3 = [1, 35, 92, 55, 25, 10, 79]
max_number = reduce(lambda x, y : x if x > y else y, numbers3)
print(max_number)


# Using list comprehension instead of map and filter
numbers4 = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]  # Filter
squared = [x ** 2 for x in numbers]               # Map

'''
Function     Input	                Output	                     Typical Use Case
           |                       |                           |
filter()   | Iterable + Condition  | Filtered elements	       | Select elements based on a condition
           |                       |                           |
map()	   | Iterable + Function   | Transformed elements	   | Apply a transformation
           |                       |                           |
reduce()   | Iterable + Function   | Asingle accumulatedresult | Compute a cumulative result
'''
