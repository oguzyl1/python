#Walrus operatörü (:=) : Python 3.8'de tanıtılan bir atama operatörüdür.
#                        Bu operatör, bir ifadeyi değerlendirirken aynı anda bir değişkene atama yapmayı sağlar.
#                        Özellikle bir ifadeyi birden fazla kez kullanmanın gerektiği durumlarda veya uzun ifadelerin 
#                        daha okunaklı bir şekilde yazılmasını sağlamak için kullanılır.


"""
foods = list()

while True:
    food = input("What food do you like?: ")
    
    if food == "quit":
        break

    foods.append(food)
"""

    #yukarıdaki kodu bu operatör ile bu şekilde kullanabiliriz
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

