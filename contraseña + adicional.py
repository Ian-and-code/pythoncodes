import random
import string as s
import time

def pg():
    chars = s.ascii_letters + s.digits + s.punctuation
    return ''.join(random.choice(chars) for x in range(4, 12))
    
password = pg()
print(password)

intento = input("intoduce una contraseña: ")
if intento == password:
    print("correcto")
else:
    print("incorrecto")
    print(intento,"/", password)
#adicional
time.sleep(10)
print("dispositivo hackeado")
time.sleep(2)
print("es broma :b")