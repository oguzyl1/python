# kwargs parametresi: Bir fonksiyonun değişen miktarlarda anahtar kelime argümanlarını kabul edebilmesi için
#                     tüm argümanları bir sözlüğe(dict) paketleyecek kullanışlı parametre


def hello(**kwargs):
    #aşağıdaki açıklama bu kod için: 
    #print(f"hello {kwargs['first']} {kwargs['last']}")

    print("hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

    

    #kwargs kullanmasaydık middle parametresi olmadığından dolayı hata alacaktık
#hello(first="Oğuz",middle="Han",last="Yıldız")
        
hello(first="Oğuz",middle="Han",last="Yıldız",abc="asdf")

