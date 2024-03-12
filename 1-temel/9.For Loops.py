import time

    #range(start,stop,step) şeklinde bir yapıdır burada start'ı girmezsek 0 dan başlar , step'i girmezsek 1 kabul eder
for i in range(10):
    print(i+1)


    #50 den başlayıp 2 şer 2 şer atlayarak 100 e kadar sayar , 101 dahil değildir 
for i in range(50,100+1,2):
    print(i)


    #string ifadeler de karakter karakter bir dizi olduğundan i burada karakterleri tek tek dolaşır ve print ile ekrana yazdırır
for i in "Oğuzhan Yildiz":
    print(i)


    #time sınıfından sleep fonksiyonunu kullanarak döngünün saniyede bir dönmesini sağlayarak bir sayaç oluşturuyoruz
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Geri sayım bitti")