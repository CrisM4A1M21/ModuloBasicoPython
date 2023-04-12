nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

nombre_completo = nombre + " " + apellido

print("Tamaño de mi nombre completo: {}".format(len(nombre_completo)))

print("Nombre completo: {}".format(nombre_completo.upper()))

if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor que el apellido")
else:
    print("El tamaño del nombre es menor que el apellido")