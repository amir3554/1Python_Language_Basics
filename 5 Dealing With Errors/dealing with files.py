file2 = open("sample2.txt", "w")  # فتح ملف في وضع الكتابة و ان لم يوجد يعمل ملف جديد
file2.write("Hello! , This text is written by Python.\n")#file = open("example.txt", "r")  # فتح ملف في وضع القراءة
file2.write("Python is great programming language!.")
file2.close()

file3 = open("sample3.txt", 'r')

print(file3.read())
print(file3.read(3))#it will read the first 3 letters only 

file3.close()

file4 = open("sample4.txt", 'r')

print(file4.readline())
print(file4.readline())
print(file4.readline())#for reading one line , and if there is no line it will return empty line
print("--------------")
print(file4.readlines())#for readin all lines
print("--------------")
#الكائن الذي تعيده الدالة اوبين هو كائن قابل ل التكرار 

for line in file4:
    print(line, end = ' ' )

file4.close()

# we use ""with"" the key word to close the file automaticly
# ""with"" has its own software block كتلة برمجية

with open("sample5.txt", 'r') as file5:
    print(file5.read())

# we must use append to add text to the file , because the function write delete all the previos data of the file and write new one.

with open("sample2.txt", 'a') as file6:
    file6.write("This is a new line.")
    
with open("sample2.txt", 'r') as file7:
    print(file7.readlines()) 

with open("sample6.txt" , 'r') as file8, open("sample7.txt" , 'w') as file9:
    f_lines = file8.read()
    file9.write(f_lines)
