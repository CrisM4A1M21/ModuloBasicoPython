paises = ["Peru","Uruguay","Venezuela","España","Mexico"]

print("los valores de mi lista actual son: {}".format(paises))

paises.insert(3,"Rusia")

print("los valores de mi lista actual son: {}".format(paises))

paises.remove(paises[0])
print("los valores de mi lista actual son: {}".format(paises))

lista1 = [40,27,83,210,22]
lista1.insert((len(lista1)),"Hola")
print("Lista1: {}".format(lista1))
lista1.clear()
print("Lista1: {}".format(lista1))