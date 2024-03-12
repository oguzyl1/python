"""

    #kendi oluşturduğumuz mesaj sınıfını çağırıyoruz
import message as msg

msg.hello()
msg.bye()

"""

    # bu şekilde çağırırsak
from message import *

    #doğrudan bu şekilde de kullanabiliriz
hello()
bye()
