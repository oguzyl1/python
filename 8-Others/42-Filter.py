# filter() fonksiyonu: belirtilen bir koşulu sağlayan elemanları içeren yeni bir iterable nesne oluşturur.
#                      Bu koşul, bir fonksiyon veya lambda ifadesi ile belirtilebilir ve 
#                      sadece koşulu sağlayan elemanlar filtrelenir.

#
# filter(function, iterable)
#


friends = [("Funda",19),
            ("Kadir",18),
            ("Oğuzhan",17),
            ("Berkay",16),
            ("Ahmet",21),
            ("Ali",20)]


age = lambda data : (data[1]>=18)

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i)