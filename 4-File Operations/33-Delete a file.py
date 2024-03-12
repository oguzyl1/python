import os
import shutil

path = "C:\\Users\\Lenovo\\Desktop\\python\\4-File Operations\\test.txt"

try:
    os.remove(path)
    #os.rmdir(path) #delete a file or empty folder
    #shutil.rmtree(path) #delete file and or folder

except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("That folder contains files")
else:
    print(f"{path} was deleted")
