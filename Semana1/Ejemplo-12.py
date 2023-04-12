"""Operadores aritmeticos en python"""

division_1 = 100/20 #float en java saldria un int
division_2 = 105.6/10 #aqui igual
division_3 = 400.4/2.0

print(division_1)
print(division_2)
print(division_3)

"""Excepcion y error de division entre 0"""

try:
    division_4 = 400 / 0
    print(division_4)
except:
    print("No se puede dividir entre 0")

print(int(division_1))