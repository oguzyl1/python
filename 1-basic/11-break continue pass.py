#break: döngüyü tamamen sonlandırmak için kullanılır
#continue: döngüde diğer iterasyona geçmek için kullanılır 
#pass: hiçbir şey yapmaz, dögüde yer tutucu görevi görür


    #isim girildiyse döngüyü sonlandırır
while True:
    name = input("Enter your name: ")
    if name != "":
        break


phoneNumber = "123-456-789"

    # - işaretine geldiği zaman if içine giriyor ve continue ile birlikte döngünün geri kalanını es geçip diğer adıma geçiyor
for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")

    #13 sayısına geldiiğinde pass geçiyor ama döngünün içinde geri kalan kısımları okumaya devam ediyor böylece 13 atlanmış oluyor 
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
    
