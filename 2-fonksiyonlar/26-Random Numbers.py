import random

    #bizim girdiğimiz aralıkta tam rakamları random olarak atar
x = random.randint(1,6)

    #0 dahil 1 dahil değil aralığında bir sayı verir
y = random.random()

    #girdiğimiz listeden rastgele eleman seçer
myList = ["taş","kağıt","makas"]
z = random.choice(myList) 

    #listenin elamanlarını karıştırır ve indexler değişir
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
