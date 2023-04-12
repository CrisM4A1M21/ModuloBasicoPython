"""
15. Crear 3 varaibles, nombre, edad y distrito
Requisitos:
- Nombre: string, edad: int, distrito:string
- concatenar estos 3 datos e indicar una oracion como la siguiente: Jose tiene x años y es del distrito de
- Obtener el modulo de su edad al usarlo con el numero 5

"""

nombre = "Cristian"
edad = 22
distrito = "S.M.P"

print('{} tiene {} años y es del distrito de {}'.format(nombre, edad, distrito))

print("El modulo de la edad entre 5 es: {}".format(edad % 5))

