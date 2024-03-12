# copyfile() --> dosyanın içeriğini kopyalar
# copy() --> copyfile() + permission mod + hedef dizin
# copy2() --> copy() + metadata'ları da kopyalar (oluşturulma ve değiştirilme zamanı )

import shutil

shutil.copyfile("C:\\Users\\Lenovo\\Desktop\\python\\4-File Operations\\test.txt","copy.txt")
