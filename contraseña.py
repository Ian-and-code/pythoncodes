c = "1234"
u = ""

while u != c and contador < 5:
    u = input("contraseña: ")
    contador = 0
    if u != c:
        print("incorrecta")
        contador = contador + 1
        if contador = 5:
           contador = "no"
           break
else:
    print("correcta")     
if contador == "no":
    print("intenta mas tarde")