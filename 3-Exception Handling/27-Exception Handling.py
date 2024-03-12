#hata işleme: programın işleyişi sırasında programı tamamen devre dışı bırakacak durumları yakalayarak programın çalışmasına devam
#             etmesini sağlarız

try:
        #burada bölene 0 girdiğimizde program hata alır ve çalışmayı durdurur 
    num1 = int(input("Bölümü gir: "))
    num2 = int(input("Böleni gir: "))
    result = num1/num2
    #bu sayede program akışında sıkıntı olduğunda program durmayacak ve bu hata mesajını alıp çalışmaya devam edecek
except ZeroDivisionError as e:
    print(e)
    print("Bölen sıfır olamaz!!")

except ValueError as e :
    print(e)
    print("Lütfen sadece rakam girin!!")

except Exception as e :
    print(e)
    print("Bir şeyler yanlış gitti :(")

    #yukarıdaki hataları almazsan bu bloğu çalıştır
else:
    print(result)

    #bu blok her türlü çalışacak hata verse de vermese de
finally:
    print("finally bloğu")
