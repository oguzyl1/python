name = "oğuzhan yildiz"
name2 = "1234567989"    


    #uzunluk metodu
print(len(name))  
                
    #aradağımız harfin veya sayının soldan sağa şekkilde ilk olarak hangi indexte olduğunu söyler
print(name.find("y"))

    #ilk harfi büyütmeye yarar
print(name.capitalize())

    #tüm harfleri büyütmeye yarar
print(name.upper())

    #bütün harfleri küçültmeye yarar
print(name.lower())

    #string dizisinin bütün ifadeleri rakamlardan oluşuyorsa true döndürür aksi halde false döner
print(name.isdigit())
print(name2.isdigit())

    #isdigit'in tam tersi tüm ifadeler alfabetik ise true aksi halde false döner(boşluk varsa da false döner)
print(name.isalpha())

    #istediğimiz karakterden kaç tane olduğunu döndürür
print(name.count("i"))

    #istediğimiz karakteri istediğimiz karakter ile değiştirmeye yarar
print(name.replace("i","ı"))

    #bir integer ile çarpıp o sayı kadar ekrana yazdırma
print(name*4)