# and , or , not 
# and: tüm şartların sağlanması lazım 
# or: şarttan biri sağlansa da olur 
# not: şart yanlışsa doğru yapar doğruysa yanlış

temp = int(input("What's the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!\nStay inside!!")
elif not(temp < 0 or temp >30):
    print("The temperature is good today!\nGo outside!!",)

