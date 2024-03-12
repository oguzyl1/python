#args parametresi : Bir fonksiyonun değişen miktarda argümanı kabul edebilmesi için tüm argümanları
#                   kullanışlı bir demet(tuple) içine paketleyecek parametre


def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0

    for i in stuff:
        sum +=i

    return sum

    #girilen parametre sayısı önemli değil istediğin kadar parametre girebilirsin işlemler ona göre yapılacak
print(f"toplam1: {add(1,2,3,4,5)}") 

print(f"toplam2: {add(1,2,3,4,5,6,7,8,9)}") 