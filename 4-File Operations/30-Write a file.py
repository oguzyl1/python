text = "\nMerhaba\nBu bir metindir.\nGuzel bir metin\n\n"

"""
    #ikinci parametre de w:write r:read gibi işlemleri girebiliriz burada açtık ve yazma işlemi yapacağız
    ancak burada kullandığımız w dosyanın üzerine yazarken dosyanın içeriğini tamamen değiştirp texti yazar
with open("C:\\Users\\Lenovo\\Desktop\\python\\4-File Operations\\test.txt","w") as file:
    file.write(text)

"""

    #bu şekilde kullanırsak orjinale dokunmayıp en sona ekleme yapar (a: append)
with open("C:\\Users\\Lenovo\\Desktop\\python\\4-File Operations\\test.txt","a") as file:
    file.write(text)