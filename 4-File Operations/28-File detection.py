import os

path = "C:\\Users\\Lenovo\\Desktop\\python\\4-File Operations\\test.txt"

    #eğer yol var ise
if os.path.exists(path):
    print("that location exists!")
    
        #yoldaki dosyanın dosya olup olmadığını kontrol etmek için
    if os.path.isfile(path):
        print("This is a file")

        #yoldaki dosyanın klasör olup olmadığını kontrol etmek için
    elif os.path.isdir(path):
        print("This is a directory") 

    
else:
    print("that location doesn't exists")