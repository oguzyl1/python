#kalıtım : bir sınıfta bulunan özellikleri başka bir sınıfın içinde tanımlamadan kullanma
#           Bu, kodun tekrar kullanılabilirliğini artırır ve programcının daha az kod yazarak daha fazla iş yapmasına olanak tanır.


    #miras veren sınıfımız
class Animal:

    alive = True

    def eat(self):
        print("The animal eating")

    def sleep(self):
        print("This animal is sleeping")

    #kalıtım bu şekilde verilir 
class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")


hawk = Hawk()
    #kalıtım aldığı sınıfın özelliğini direkt olarak çağırabiliyoruz
print(hawk.alive)
hawk.eat()
hawk.sleep()


hawk.fly()