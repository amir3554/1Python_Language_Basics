import sys

if sys.platform.startswith("win32"):
    print("You are using Windows.")
elif sys.platform.startswith("darwin"):
    print("You are using macOS.")
elif sys.platform.startswith("linux"):
    print("You are using Linux.")

print(sys.version)

if (sys.version.startswith('3. 9 .5')):
    print("Python System is up to date.")
else:
    print("Please update.")

print(sys.getwindowsversion())

import os

print(os.getcwd())

os.chdir("Folder1")

print(os.getcwd())

print(os.chdir("../forlder2"))

print(os.getcwd())

os.chdir("..")

print(os.getcwd())

print(os.listdir())

print(os.scandir())

content = os.scandir()

for item in content:
    print(item.name)

for item in content:
    if not item.is_file():
        continue
    else:
        print(item.name)

os.mkdir("Folder4")

try:
    os.mkdir("Forlder5")
except FileExistsError as e:
    print("oh uh", e)

os.makedirs("Folder1/folder2")

os.rename("Folder5", "Forlder5.1")

#os.rmdir("Folder5")
