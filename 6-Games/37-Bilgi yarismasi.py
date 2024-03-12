#----------------------------


def new_game():
    guesses = []
    correct_guesses = 0
    questio_num = 1

    for key in question:
        print("---------------------")
        print(key)
        for i in options[questio_num-1]:
            print(i)

        guess = input("Cevap (A, B, C, D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key),guess)
        questio_num += 1

    display_score(correct_guesses,guesses)
        


#----------------------------


def check_answer(answer ,guess):
    
    if answer == guess:
        print("Doğru")
        return 1
    else:
        print("Yanlış")
        return -0


#----------------------------


def display_score(correct_guesses,guesses):
    print("-------------------------")
    print("Sonuç")
    print("-------------------------")

    print("Answers: ",end="")
    for i in question:
        print(question.get(i), end=" ")
    print()


    print("Guesses: ",end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(question))*100)
    print("Skorun: " +str(score)+"%")

#----------------------------



def play_again():
    
    response = input("Tekrar oynamak ister misin?: (evet veya hayır): ").lower()

    if response == "evet":
        return True
    else:
        return False


#----------------------------

question = {
    "Python'u kim yarattı? ":"A",
    "Python kaç yılında yaratıldı? ": "B",
    "Python hangi komedi grubuna ithaf edilmiştir? ":"C",
    "Dünya dönüyor mu? ":"A"
}

options = [
    ["A. Guido van Rossum","B. Elon Musk","C. Bill Gates","D. Mark Zuckerberg"],
    ["A. 1989","B. 1991","C. 2000","D. 2016"],
    ["A. Lonely Island","B. Smosh","C. Monty Python","D. SNL"],
    ["A. Doğru","B. Yanlış","C. Bazen","D. Dünya ne?"],
    ]


new_game()

while play_again():
    new_game()    

print("Güle Gülee")