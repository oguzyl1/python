#listeler : birden fazla öğeyi tek bir değişkende depolamak için kullanılır

food = ["pizza","hamburger","hotdog","makarna","puding"]

    #doğrudan index ile içerideki değişken değiştirilebilir
food[0] = "suşi"

    #sona eleman ekleme
food.append("dondurma")

    #eleman silme
food.remove("hotdog")

    #sondan eleman silme
food.pop()

    #istenilen indexe eleman ekleme
food.insert(2,"kek")

    #listeyi alfabetik olarak sıralama (a dan z ye)(0 dan ileriye)
food.sort()

    #listenin içindeki elamanların hepsini silme
food.clear()

    #for döngüsü ile elamanları yazdırma
for i in food:
    print(i)

    #listede bu şekilde birden fazla farklı türde değişkeni bir arada kullanabiliriz
list2=["abc",5,True,2.0,5j]

