import os

source = "text.txt"
destination = "C:\\Users\\Lenovo\\Desktop\\python\\4-File Operations\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print("{source} was moved")

except FileNotFoundError:
    print(f"{source} was not found")