# super() :bir alt sınıfın (subclass) üst sınıfının (superclass) metotlarını çağırmak için kullanılır.
#          Bu, alt sınıfın özel durumları işlerken üst sınıfın işlevselliğinden yararlanmayı sağlar.


class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class Square(Rectangle):
        
        # uzunluk ve genişliği kare hesaplarken de kullanacağımız için tekrar tanımlamakla uğraşmadan kurucu metod içine 
        # super fonksiyonu ile direkt olarak çektik  
    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        return self.lenght*self.width
    
class Cube(Rectangle):
    
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def volume(self):
        return self.lenght*self.width*self.height


square = Square(2,4)
print(square.area())

cube = Cube(3,5,2)
print(cube.volume())