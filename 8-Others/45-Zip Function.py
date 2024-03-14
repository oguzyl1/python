#zip(*iterable) fonksiyonu:  bir veya daha fazla iterable nesneyi alır ve bu nesnelerin elemanlarını gruplar.
#                            Her bir grup, aynı konumda bulunan elemanlardan oluşur. Sonuç olarak, bu gruplar birleştirilerek 
#                            bir zip nesnesi oluşturulur veya zip nesnesinin elemanları çeşitli biçimlerde kullanılabilir. 

usernames = ["Funda","Oğuz","Berkay"]
passwords = ["p@ssword","abc123","zxcv147"]

    #indexlerine göre birbiri ile eşleşti , sınırsız değişkenle zipleme yapılabilir
users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(f"{key} : {value}")

