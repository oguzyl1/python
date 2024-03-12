try:
        #dosya bu şekilde açılır eğer dosya proje dosyasının içinde ise direkt olarak test.txt şeklinde de yazılabilir
    with open("C:\\Users\\Lenovo\\Desktop\\python\\4-File Operations\\test.txt") as file:
            #açılan dosyayı okumaya yarar
        print(file.read())

except FileNotFoundError:
    print("That file was not found :(")