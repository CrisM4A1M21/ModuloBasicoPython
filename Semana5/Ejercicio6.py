from datetime import datetime, date

""" Obtener la fecha actual """

fecha = date.today()

print(f"La fecha de hoy es: {fecha}")

tiempo = datetime.now()

print(f"{tiempo}")

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("Año actual: {}".format(anio))
print("Mes actual: {}".format(mes))
print("Dia actual: {}".format(dia))



hora = tiempo.hour
minuto = tiempo.min
segundo = tiempo.second

print("Hora actual: {}".format(hora))
print("Minuto actual: {}".format(minuto))
print("Segundo actual: {}".format(segundo))
