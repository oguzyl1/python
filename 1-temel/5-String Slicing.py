# slicing = bir diziden öğeler çıkararak bir alt dizi oluşturur
#           indexing[] ya da slice()   
#           [başlangıç:bitiş:adım]
#           adım: örn:2 verirsek başlangıç noktasında 2 2 atlayarak ilerler


#
# indexing[]
#
name = "Oğuzhan Yildiz"

    # name[:8] şeklinde de yazılabilir bu şekilde kullanımda başalngıç 0 kabul edilir
firstName = name[0:8]

lastName = name[8:15]

    #[::2] bu şekilde yazarsak başlangıç indexini 0 bitiş indexini de en son index olarak kabul eder
funkyName = name[0:8:2]

    #cümleyi tersten yazdırma
reversedName = name[::-1]


#
#slice()
#

website1 = "http://google.com"
website2 = "http://wikipedia.com"

    #bir kural belirleriz bu kuralı direkt olarak indexing içine yazıp farklı yerlerde kullanabiliriz
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])