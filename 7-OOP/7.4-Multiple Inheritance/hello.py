#çoklu kalıtım: bir alt sınıf (child class) birden fazla evebeyn sınıftan (parent class) kalıtım alabilir

class Prey:

    def flee(self):
        print("This animal fless")

class Preadator:

    def hunt(self):
        print("This animal hunting")

class Rabbit(Prey):
    pass

class Hawk(Preadator):
    pass

    #Fish sınıfı çoklu kalıtım aldı iki parent sınıfında özelliklerine erişebilir
class Fish(Prey,Preadator):
    pass


fish1 = Fish()
fish1.flee()
fish1.hunt()

