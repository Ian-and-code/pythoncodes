from datetime import datetime

def calcular_dias_restantes(fecha_objetivo):
  """
  Calcula los días restantes hasta una fecha específica.

  Args:
    fecha_objetivo: Una cadena que representa la fecha en formato 'YYYY-MM-DD'.

  Returns:
    Un entero representando los días restantes, o None si la fecha objetivo es inválida.
  """
  try:
    fecha_actual = datetime.now()
    fecha_objetivo_dt = datetime.strptime(fecha_objetivo, '%Y-%m-%d')
    diferencia = fecha_objetivo_dt - fecha_actual
    return diferencia.days
  except ValueError:
    return None

print("AAAA-MM-DD")
z = input("fecha: ")
print(z)
# Ejemplo de uso
fecha_objetivo = z
dias_restantes = calcular_dias_restantes(fecha_objetivo)

if dias_restantes is not None:
  print(f"Faltan {dias_restantes} días para {fecha_objetivo}")
else:
  print("Formato de fecha inválido. Usa YYYY-MM-DD.")