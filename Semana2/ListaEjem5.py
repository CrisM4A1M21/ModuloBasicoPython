paises = []
paises.append("Peru")
paises.append("Brasil")
paises.append("Canada")
paises.append("Alemania")

print("Mi lista actual es: {}".format(paises))

print("El pais de mi lista con posicion 1 es: {}".format(paises[1]))
print("El pais de mi lista con posicion 3 es: {}".format(paises[3]))

edades =[34,13,13,11,13,11,14,13]
print("El indice de mi posicion 2 es: {}".format(edades[2]))

actualizar = edades[2] + 10
edades[2] = 27
edades[2] = edades[2] + 15
print("Mi lista actualizada es: {}".format(edades))