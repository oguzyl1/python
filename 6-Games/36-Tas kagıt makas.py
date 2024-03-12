import random


while True:
    secimler = ["taş","kağıt","makas"]

    computer = random.choice(secimler)
    player = None

    while player not in secimler:
        player = input("taş, kağıt ya da makas?: ").lower()

    
    if player == computer:
        print(f"computer: {computer}\nplayer: {player}\nBerabere!!")
    
    elif player == "taş":
        if computer == "kağıt":
            print(f"computer: {computer}\nplayer: {player}\oyuncu kazandı!!")
        elif computer == "makas":
            print(f"computer: {computer}\nplayer: {player}\nbilgisayar kazandı!!")
        else:
            print(f"computer: {computer}\nplayer: {player}\nBerabere!!")

    elif player == "kağıt":
        if computer == "makas":
            print(f"computer: {computer}\nplayer: {player}\oyuncu kazandı!!")
        elif computer == "taş":
            print(f"computer: {computer}\nplayer: {player}\nbilgisayar kazandı!!")
        else:
            print(f"computer: {computer}\nplayer: {player}\nBerabere!!")

    elif player == "makas":
        if computer == "kağıt":
            print(f"computer: {computer}\nplayer: {player}\oyuncu kazandı!!")
        elif computer == "taş":
            print(f"computer: {computer}\nplayer: {player}\nbilgisayar kazandı!!")
        else:
            print(f"computer: {computer}\nplayer: {player}\nBerabere!!")

