#tuple: İlgili verileri bir arada gruplamak için kullanılan, sıralı ve değiştirilemez koleksiyon

student = ("Oğuzhan",21,"male")

    #tuple da kaç tane oğuzhan olduğunu döndürür
print(student.count("Oğuzhan"))

    #belirtilen elemanın indexini verir
print(student.index("male"))

    #for dögüsü kullanarak yazdırma 
for i in student:
    print(i)

    #if bloğunun kullanımı için farklı bir örnek 
if "Oğuzhan" in student:
    print("Oğuzhan is here!")

    