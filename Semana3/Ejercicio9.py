ingenierias = ["Sistemas","Software","Minas","Electrica","Electronica"]

print("El tamaño de mi lista es: {}".format(len(ingenierias)))
i=0
for ing in ingenierias:
    print(ing)
    print("esta es la vuelta {}".format(i))
    i = i + 1

print("------------------------------------------")
for i in range(0, 10):
    print(i)

"""Usando if ternario"""

estado = 0
final = "1. Su estado final es teminado" if estado == 0 else "2. Su estado no es terminado"
print(final)
