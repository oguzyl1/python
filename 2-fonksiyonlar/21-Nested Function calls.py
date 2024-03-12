#iç içe fonksiyonlar: fonksiyonları iç içe kullanabiliriz. Program çalışmaya başladığında en içteki fonksiyondan başlayarak
#                     dışarıdaki fonksiyona doğru devam eder içteki fonksiyonun döndürdüğü değer içinde olduğu fonksiyonun 
#                     parametresi olarak aktarılır


"""
bu şekilde kullanmak yerine aşşağudaki gibi kullanım kod okunurluğu açısından daha iyi olabilir (her zaman değil)

num = input("Bir pozitif sayı gir: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

"""

print(round(abs(float(input("bir pozitif sayı gir: ")))))