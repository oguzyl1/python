# değişkenlerin tanımlandıkları kapsam dahilinde kullanılmasını sağlar


    #global scope : sınıf içinde her yerden erişilebilir 
name = "Oğuzhan"

def display_name():
        #local scope: Bir fonksiyonun içinde oluşturulan değişken, o fonksiyonun yerel kapsamına aittir 
        #             ve yalnızca o fonksiyonun içinde kullanılabilir. 
    name = "Yıldız"
    print(name)

    #fonksiyon içindeki name ile dışındaki name farklı veriler tutuyor
display_name()
print(name )

