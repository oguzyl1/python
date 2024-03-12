#iç içe geçmiş dögüler

rows =  int(input("satır sayısını gir: "))
columms = int(input("sütun sayısını gir: "))
symbol = input("Kullanılacak sembolü gir: ")

for i in range(rows):
    for j in range(columms):
        print(symbol, end="")
    print()


