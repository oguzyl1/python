#abstract sınıflar: içerisinde en az bir tane abstract metod bulunan ve doğrudan örneklenemeyen sınıflardır.
#                   Abstract metodlar ise sadece tanımlanır, içerikleri belirtilmez ve alt sınıflar tarafından
#                   zorunlu olarak uygulanmalıdır. Bu, alt sınıfların belirli bir davranışı uygulamasını sağlar,
#                   ancak bu davranışın nasıl uygulanacağı abstract sınıfın alt sınıflarına bırakılır. 
#                   Bu sayede soyutlamalar yapılabilir ve kodun daha modüler ve genişletilebilir olması sağlanır.



    # abc modülü, Python'da soyut temel sınıflar (ABC) ve soyut metotlar tanımlamak için kullanılır;
    # ABC sınıfı soyut sınıfları oluştururken, abstractmethod dekoratörü soyut metodları tanımlar ve
    # alt sınıfların bu metotları uygulamasını zorunlu kılar.
from abc import ABC , abstractclassmethod

    #ABC sınıfında kalıtım aldırdık
class Vehicle(ABC):

        #metodun abstract olduğunu belirttik
    @abstractclassmethod
    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("You drive a car")

    def stop(self):
        print("This car is stopped ")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")
   
    def stop(self):
        print("This motorcycle is stopped ")

"""
    #abstract bir sınıftan obje oluşturamayız bu şekilde kullanmaya çalışırsak program hata verecektir
vehicle = Vehicle()
vehicle.go()

"""

car = Car()
car.go()
car.stop()

print("--------------------")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()




# abstract sınıflar neden kullanılmalı? : Abstract sınıflar ve metodlar, bir arayüzün belirlenmesi ve 
#                                         bu arayüzü uygulayan sınıfların davranışlarının standartlaştırılması için kullanılır. 
#                                         Bu, kodun daha modüler, yeniden kullanılabilir ve genişletilebilir olmasını sağlar. 
#                                         Özellikle bir kod tabanında farklı sınıfların belirli bir davranışı paylaşması
#                                         gerekiyorsa veya bir sınıfın belirli metodları zorunlu olarak uygulaması gerekiyorsa 
#                                         abstract sınıflar ve metodlar kullanılabilir. Bu sayede, kodun daha organize olması,
#                                         hataların azalması ve daha esnek bir yapı oluşturulması sağlanır.