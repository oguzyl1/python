#set(küme): verileri içinde sırasız ve indexlenmemiş şekilde tutar her yazdırıldığında farklı bir sıra ile yazdırılır.
#           Yinelenen değeri tekrar yazdırmaz


utensils = {"çatal","kaşık","bıçak","bıçak"}
dishes = {"tabak","kase","bardak","bıçak"}


"""
    #eleman eklemek için
utensils.add("tuzluk")

    #eleman silme
utensils.remove("çatal")

    #tamamen temizlemek için
utensils.clear()

    #iki set'i birleştirir
utensils.update(dishes)

"""

"""
    #Her iki kümedeki tüm öğeleri içeren yeni bir küme döndüren union() yöntemi veya  
    #bir kümedeki tüm öğeleri diğerine ekleyen update() yöntemi kullanılarak kümeler birleştirilir.
dinnerTable = utensils.union(dishes)

for i in dinnerTable:
    print(i)

"""    

    #iki set arasındaki farklı elemanları döndürür
print(utensils.difference(dishes))

    #iki set arasında kesişen elemanları döndürür
print(utensils.intersection(dishes))