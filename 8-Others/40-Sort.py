# sort() method -->  listeyle birlikte kullanılır
# sort() function --> iterasyon işlemi sırasında kullanılır 

students = (("Funda","F",60),
            ("Kadir","A",33),
            ("Oğuzhan","D",36),
            ("Berkay","B",20),
            ("Ahmet","C",78))


    #bir lambda fonksiyonu tanımladık ve bu grades parametresi alacak, bu parametrede de 1. index'i döndürecek 
grade = lambda grades:grades[1]

    #sorted fonksiyonunda students tuple'ını verdik ve key parametresi de lambda foknsiyonunu notlarına göre([1]) sıralar
sorted_students = sorted(students,key=grade)

    #yazdırma işlemi
for i in sorted_students:
    print(i)


#-------------------------------------------------------#
print("-----------------------------")
students2=["Funda","Kadir","Oğuzhan","Berkay","Ahmet"]
    #a-z sıralama
students2.sort()

    #z-a sıralama
students2.sort(reverse=True)

for i in students2:
    print(i)