#Lambda fonksiyonları: anonim (isimsiz) fonksiyonlar olup, tek bir ifadeyle sınırlı ve
#                      genellikle küçük fonksiyonlar için kullanılır. 
#                      Kısa ve hızlı bir şekilde fonksiyon tanımlamak için kullanılırlar ve genellikle
#                      map(), filter(), reduce() gibi yerleşik fonksiyonlarla birlikte kullanılırlar.


double = lambda x: x*2
multiply = lambda x,y: x*y
add = lambda x,y,z: x+y+z
full_name = lambda first_name , last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False

    # lambda da tanımladığımız x yerine verdiğimiz parametre gider 
print(double(5))

print(multiply(5,3))

print(full_name("Oğuzhan","Yıldız"))

print(age_check(21))