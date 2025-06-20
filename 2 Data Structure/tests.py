'''
numbers = [2, 5, 7, 1, 3, 4] 
resault = 1
fin = 1

for num in numbers :
   fin = num * resault
   resault = fin

resault2 = 1

for number in numbers :
   resault2 = number * resault2

print(fin)
print(resault2)
'''
#============================
#[a, a+b, a+b+c, a+b+c+d]
'''
numbers = [4, 6, 2, 5]
my_numbers = []
sum = 0
 ###
for index, number in enumerate(numbers) :
    my_numbers.append(num)
    num = my_numbers[index] + num
print(my_numbers)
'''
'''
for number in numbers :
    sum = sum + number
    my_numbers.append(sum)

print(my_numbers)
'''
numbers = [1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9, 10, 12]
'''dub_num = {'singular': 0, 'dub' : 0}
my_num_list = []
dub_list = []
for number in numbers :
    if number in my_num_list:
        dub_num['dub'] += 1
        dub_list.append(number)
    else:
        dub_num['singular'] +=1 
    my_num_list.append(number)

print(dub_list)
''''''
nums_dict = {}
dups =[]

for number in numbers :
    if number in nums_dict:
        nums_dict[number] += 1
        dups.append(number)
    else:
        nums_dict[number] = 1
print(nums_dict)
print(dups)
'''

fruits = ['lemon', 'pinapple', 'apple', 'orange', 'banana', 'grape']

fruit_dict = {}

for fruit in fruits:
    fruit_dict[fruit] = len(fruit)
fruit_char_count = {i : len(i) for i in fruits}
print(fruit_dict)
print(fruit_char_count)



gruop_nums = []
for i in range(0, len(numbers), 3):
    gruop_nums.append(numbers[i: i +3])
    
print(gruop_nums)
size = 3
nums_list = [numbers[i: i + size] for i in range(0, len(numbers), size)]

print(nums_list)

