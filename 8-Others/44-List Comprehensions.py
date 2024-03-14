# List comprehensions: Python'da kısa ve okunaklı bir şekilde liste oluşturmayı sağlayan bir yapıdır. 
#                      Bir iterable nesne üzerinde döngü yaparak ve her bir elemana belirli bir işlem uygulayarak
#                      yeni bir liste oluşturur. Bu yapı, genellikle tek satırda ifade edilir ve listeleri oluştururken
#                      daha temiz ve etkili bir yaklaşım sunar.


"""
    #bu kadar satır kod yerine aşağıdaki yöntem ile tek satırda bu işlemi yapabiliriz
squares = []

for i in range(1,11):
    squares.append( i * i )

print(squares)

"""

squares = [ i * i for i in range(1,11)]
print(squares)


    #lambda işlemlerini de bu kalıpla birlikte kullanabiliriz

students = [100,90,80,70,60,50,40,30,0] 
passed_students =list(filter(lambda x: x>60,students))
print(passed_students)

    #aynı şekilde if else işlemlerini de yapabiliriz
passed_students2 = list( i if i>=60 else "FAİLED" for i in students)
print(passed_students2)