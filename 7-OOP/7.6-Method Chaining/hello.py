# method chaining (metod zincirleme) : bir nesne üzerinde ardışık metod çağrılarını tek bir satırda zincirleme olarak 
#                                   yapmayı sağlayan bir programlama tekniğidir. Bu, kodun daha okunabilir ve kompakt olmasını sağlar.

class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brake")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

    #bu şekilde bir kullanımla tek satırda yazabiliriz
#car.turn_on().drive()


car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()


#neden "return self" yapıyoruz?: her metod çağrısından sonra return self ifadesi kullanılarak,
#                                çağrının aynı nesneye geri dönmesi sağlanır. Bu, bir nesne üzerinde ardışık metod çağrılarını
#                                zincirleme olarak yapabilmemizi sağlar. Eğer return self ifadelerini yazmazsak,
#                                ardışık metod çağrıları yaparken her seferinde yeni bir nesne oluşturulur 
#                                ve zincirleme işlemi mümkün olmaz. 