from Car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2019,"red")

 
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print("-----------------------")
    #class değişkenini car_1 için değiştirdik ama car_2 için bir şey yapmadık o direkt olarak classdaki değeri ile gelecek
car_1.whells = 2 

print(car_1.whells)
print(car_2.whells)
   
    #direkt olarak sınıf üzerinden sorgulama yaparsak yine classdaki tanımlanan değeri alırız
print(Car.whells)

    