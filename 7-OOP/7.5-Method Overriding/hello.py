# method overriding: parent sınıfta abc() diye bir fonksiyon olduğunu var sayalım ve bu fonksiyon print("parent class") yazdırsın ,
#                    child sınıf kalıtım aldığında kendi içinde abc() adında bir fonksiyon tanımlayıp bu fonksiyonun içine  
#                    print("child class") yazalım. Artık child sınıftan bir obje türettiğimiz zaman ve abc() fonksiyonunu çağırdımız
#                    zaman bize çıktı olarak "child class" çıktısını verecek. Bu durum method overriding yani metodun üzerine yazmadır.

class Animal:
    def eat(self):
        print("This animal is eatting")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
    #rabbit içinde yazdığımız fonksiyonun çıktısını verecek
rabbit.eat()

#---------------------------------------------------------------

rabbit2 = Animal()
    #animal içinde yazdığımız fonksiyonun çıktısını verecek
rabbit2.eat()

