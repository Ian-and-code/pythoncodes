def división(a, b):
    if b != 0:
        return a / b
    else:
        print("división entre 0 prohibida")

def radic(a, b):
    if b != 0:
        return pow(a, 1/b)
    else:
        print("no raiz a la 0 potencia")
a = input("a: ")
print(a)
print("")

b = input("b: ")
print(b)
print("")

print("suma: ", float(a) + float(b))
print("")
print("resta: ", float(a) - float(b))
print("")
print("mult: ", float(a) * float(b))
print("")
print("div: ", división(float(a), float(b)))
print("")
print("elev: ", pow(int(a), int(b)))
print("")
print("radic: ", radic(float(a), float(b)))
print("")
print("porcent: ", float(a)/100 * float(b))