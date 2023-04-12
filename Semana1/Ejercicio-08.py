""" Conversion de enteros a strings """

var_1 = 4000
var_2 = "Hello word"
var_3 = "500"

# NO es posible lo siguiente
#suma = var_1 + var_3
#print(suma)

conversion = str(var_1)
print("El valor de mi variable conversion es: {}".format(conversion))
print("El tipo de dato de mi variable conversion es: {}".format(type(conversion)))

conversion_2 = int(var_3)
print("El valor de mi variable conversion es: {}".format(conversion_2))
print("El tipo de dato de mi variable conversion es: {}".format(type(conversion_2)))

suma = var_1 + conversion_2

print("El valor de mi suma es: {}".format(suma))

suma_2 = var_2 +' '+ var_3

print("El valor de mi suma es: {}".format(suma_2))
