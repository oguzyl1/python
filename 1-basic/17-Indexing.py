#index operatörü [] = dizi elamanlarına erişim verir (str, list, tuple)

name = "oğuzhan Yildiz!"

if name[0].islower():
    name = name.capitalize()

firstName = name[:8].upper()
lastName = name[8:].lower()

    #son karakteri yazdırmak için
lastCharacter = name[-1]

    #yukarıdaki işlemi sondan istediğimiz elemanı yazdırmak için çeşitlendirebiliriz
character = name[-3]

print(firstName)
print(lastName)
print(lastCharacter)
print(character)