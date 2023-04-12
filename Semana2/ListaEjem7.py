sueldos = [1000,3000,6000,8000,9000,12000]

print("Tamaño de la lista {}".format(len(sueldos)))

for i in range(len(sueldos)):
    if sueldos[i] > 8000:
        sueldos[i] = sueldos[i] + 2000

print("Sueldos: {}".format(sueldos))