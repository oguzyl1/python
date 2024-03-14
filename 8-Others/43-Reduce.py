# reduce(): fonksiyonu, bir listenin tüm elemanlarını birleştirerek veya bir işlemi uygulayarak 
#           tek bir sonuç elde etmek için kullanılır; 
#           her adımda önceki iki eleman üzerinde belirtilen bir işlem uygulanır ve sonuç bir sonraki adıma geçer.
#           Bu, veri analizi veya işlem sırasında bir değerin akümüle edilmesi için kullanılabilir.

#
# reduce(function, iterable)
#

import functools

letters = ["H","E","L","L","O"]

word = functools.reduce(lambda x, y, : x + y , letters)
print(word)


factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y, : x * y ,factorial)
print(result)




