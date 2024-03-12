# str.format() : Çıktıyı görüntülerken kullanıcılara daha fazla kontrol sağlayan isteğe bağlı yöntem

animal = "cow"
item = "moon"

    #bu şekilde bir kullanım yapabiliriz
print(F"The {animal} jumped over the {item}")

    #yukarıdaki ile aynı işlevi görür
print("The {} jumped over the {}".format(animal,item))

    #bu şekilde indexleme de yapabiliriz
print("The {1} jumped over the {0}".format(item,animal))

    #bu şekilde de kullanılabilir
text = "The {} jumped over the {}"
print(text.format(animal,item))


name = "Oğuzhan"
    #Burada {:10} ifadesi, alan genişliğini belirtir.Yani, bu ifade, belirtilen metnin en fazla 10 karakter genişliğinde olacağını belirtir. Eğer metin 10 karakterden daha kısa ise, sağa doğru boşluk eklenir. 
    # Eğer metin 10 karakterden daha uzunsa, metin kesilir veya uzunluğuna uyacak şekilde kısaltılır.
print("Hello my name is {:10}".format(name))

print("Hello my name is {:<10}. Nice to meet you!".format(name))
print("Hello my name is {:>10}. Nice to meet you!".format(name))
print("Hello my name is {:^10}. Nice to meet you!".format(name))


number = 3.14159
    #virgülden sonra kaç basamağı alacağımızı belirleriz
print("The number pi is {:.3f}".format(number))

number2 = 1000
    #sayıyı binary olarak yazdırma 
print("The number is {:b}".format(number2))

    #sayıyı sekizlik sayı sisteminde olarak yazdırma 
print("The number is {:o}".format(number2))

    #sayıyı hexedecimal olarak yazdırma 
print("The number is {:X}".format(number2))


    #sayıyı bilimsel gösterimde yazdırma 
print("The number is {:E}".format(number2))