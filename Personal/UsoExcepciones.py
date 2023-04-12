number1, number2 = 5, 1

print(number1 + number2)

try:
    resultado = number1 * number2 + " "
except TypeError as e:
    print("-------------------------------")
    print("No es el mismo tipo de dato")
    print("Mas informacion del error:")
    print("\t{}".format(e))
    print("-------------------------------")
else:
    print("Resultadod de la operacion {}".format(resultado))
finally:
    print("Ejecucion finalizada")
