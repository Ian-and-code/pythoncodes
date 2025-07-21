print("aclaraciones")
print("")

print("1. nros enteros entre 1 a 3300 en x o y")
print("2. no pueden dar exponentes muy largos")
print("incluso en anotación cientifica")
print("(ej 1.939e100)")
print("3. se usa anotación cientifica (ej 1.372e100)")
print("")

x = input("x: ")
print(x)
y = input("y: ")
print(y)
n = "no"
import math
z = 1 / float(y)
s = float(x) + float(y) 
r = float(x) - float(y) 
m = float(x) * float(y) 
d = float(x) / float(y) 
p = float(x) ** float(y)
rd = float(x) ** float(z)
ml = math.log(float(x), float(y)) 
pc = float(x)/100 * float(y)
xms = math.sin(float(x)) 
xmc = math.cos(float(x)) 
xmt = math.tan(float(x))
xmf = math.factorial(float(x)) 
xma = math.fabs(float(x)) 

inf = math.inf #infinito

pi = math.pi #pi

e = math.e #e

tau = math.tau #tau / 2pi

yms = math.sin(float(y))
ymc = math.cos(float(y))
ymt = math.tan(float(y))
ymf = math.factorial(float(y))
yma = math.fabs(float(y))
    
yms = round(yms, 4)
ymc = round(ymc, 4)
ymt = round(ymt, 4)
xms = round(xms, 4)
xmc = round(xmc, 4)
xmt = round(xmt, 4)
pc = round(pc, 4)
ml = round(ml, 4)
rd = round(rd, 4)

print("")
print("x (operador) y")
print("")

print(f"suma: {s}")
print(f"resta: {r}")
print(f"mult: {m}")
print(f"div: {d}")
print(f"pot: {p}")
print(f"radic: {rd}")
print(f"logaritmo: {ml}")
print(f"porcentaje: {pc}")

print("")
print("solo a x")
print("")

print(f"seno: {xms}")
print(f"coseno: {xmc}")
print(f"tangente: {xmt}")
print(f"factorial: {xmf}")
print(f"modulo: {xma}")

print("")
print("solo a y")
print("")

print(f"seno: {yms}")
print(f"coseno: {ymc}")
print(f"tangente: {ymt}")
print(f"factorial: {ymf}")
print(f"modulo: {yma}")

print("")
print("constantes")
print("")

print(pi)
print(tau)
print(e)
print(inf)

(f"factorial: {ymf}")
print(f"modulo: {yma}")

print("")
print("constantes")
print("")

print(pi)
print(tau)
print(e)
print(inf)lo: {yma}")

print("")
print("constantes")
print("")

print(pi)
print(tau)
print(e)
print(inf)
