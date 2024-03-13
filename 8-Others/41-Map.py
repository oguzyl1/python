# map() fonksiyonu, belirtilen bir fonksiyonu bir veya birden fazla iterable üzerinde uygulayarak yeni bir iterable nesne döndürür.
#
# map(function , itarable)


    #yanlarındaki fiyatları dolar cinsinden düşünün
store = [("tisort",20.00),
         ("pantolon",25.00),
         ("ceket",50.00),
         ("corap",10.00)]

    #lambda fonksiyonu yazdık (0,82 doları euro'ya çevirmek için)
to_euros = lambda data : (data[0],data[1]*0.82)

    #map sayesinde store listesini to_euros fonksiyonuna gönderiyoruz
store_euros = list(map(to_euros,store))

    #fiyatı sıralamak için bir lambda fonksiyonu oluşturduk
price = lambda prices:(prices[1])

    #sorted sayesinde store_euros listesi price(prices[1]) ' e göre sıraladık
sorted_store_euros = sorted(store_euros,key=price)


for i in sorted_store_euros:
    print(i)
