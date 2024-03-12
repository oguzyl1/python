name1 = ""
name2 = None

    #isim uzunluğu sıfırdan farklı olana kadar döngü döner 0 dan farklı olduğunda döngüden çıkar
while len(name1) == 0 :
    name1 = input("Enter your name: ")

print(f"hello, {name1}")

    #bu döngü de aynı işlevi görür name2=None yani boş olarak düşünelim not none dediğimizde boş olmayana kadar devam et demek oluyor
while not name2:
    name2 = input("Enter your name: ")

print(f"hello, {name2}")

    
