lista = [1,1,2,3,4,5,2,2,1,3,3,5,4,5,4]

print("Numero de repitencias de 4 es: {}".format(lista.count(4)))

lista1 = lista.copy()

lista1.reverse()

print("Lista: {}".format(lista1))

lista2 = lista.copy()

lista2.sort()

print("Lista Ordenada: {}".format(lista2))

lista3 = ["Yuji","Megumi","Nobara","Satoru","Nanami","Toji"]
print("Lista3: {}".format(lista3))
del lista3[5]
print("Lista3: {}".format(lista3))