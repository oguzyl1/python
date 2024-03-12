#multilevel inheritance, bir alt sınıfın bir üst sınıftan, o üst sınıfın başka bir üst sınıftan türediği bir kalıtım yapısıdır.

class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()

    #dog sınıfı doğrudan organism sınıfından kalıtım almamasına rağmen alive değişkenine erişebiliyor 
print(dog.alive)
