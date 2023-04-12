nombre_completo = input("Ingrese su nombre completo: ")

nom = nombre_completo.split()

print("Sus apellidos son: {}".format(nom[len(nom)-2] + " " + nom[len(nom)-1]))

