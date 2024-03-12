#Sözlük :anahtar:değer mantığı vardır anahtar benzersiz olmalıdır. Anahtar string veya integer bir ifade olabilir değer 
#        ise herhangi bir şey olabilir (int,float,tuple,dictionary,set,string...). Hash kullanıldığı için hızlıdır 

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

    #sözlüğe elaman ekler veya key değeri bulunuyorsa günceller
capitals.update({"Germany":"Berlin"})   
capitals.update({"USA":"Las Vegas"})

    #silme işlemi yapar 
capitals.pop("China")

"""
    #sözlüğü temizleme
capitals.clear()
"""

    #bu şekilde aratma yapmak daha iyi çünkü olmayan bir key girildiğinde program hata vermek yerine none döndürür
    #capital["Turkey"] --> bu şekilde aratırsan olmayan bir key ise program patlar 
print(capitals.get("Turkey"))


    #sadece key değerlerini yazdırma
print(capitals.keys())

    #sadece value değerlerini yazdırma 
print(capitals.values())

    #tüm değerleri yazdırma
print(capitals.items())

for key,value in capitals.items():
    print(key," -- ",value)