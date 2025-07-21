import random
import time

posibles = [7] * 10 + [1, 2, 3, 4, 5 ,6]

resultado = (random.choice(posibles))
print("ruleta girando")
time.sleep(2)
print(resultado)