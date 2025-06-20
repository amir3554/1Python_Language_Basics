numbers = [12, 30, 42, 67, 82, 92, 101, 2, 25, 9]

numbers50 = [number for number in numbers if number > 50]
'''
numbers50 = []
for number in numbers
    if number  50
        numbers50.append(number)
    else
        continue
'''
print(numbers50)


squares = [i**2 for i in range(11)]
print(squares)


persantages = [92, 74, 35, 101, 50, 103, 99, 100, 105]

my_persantages = [oo if oo <= 100 else 100 for oo in persantages ]
print(my_persantages)

nums = {i : i**2 for i in range(10)}
print (nums)

list_numbers = [2, 3, 3, 11, 64, 11, 9, 58, 26, 100, 35, 44, 9]

new_numbers_set = {i for i in list_numbers}
print(new_numbers_set)


matrix1 = [[i for i in range(5)] for j in range(6)]
print(matrix1)
