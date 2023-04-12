paises = []

print("El tamaño de la lista: {}".format(len(paises)))

paises.append("Peru")
paises.append("Uruguay")
paises.append("Venezuela")

print("los valores de mi lista actual son: {}".format(paises))
print("El tamaño de la lista: {}".format(len(paises)))

paises.pop()  #Elimina el ultimo pero si le pasas un parametro te elimina esa posicion
print("los valores de mi lista actual son: {}".format(paises))
