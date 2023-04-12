class Persona:

    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def getDni(self):
        return self.__dni

    def caminar(self):
        print(f"{self.nombre} esta caminando")


my_person = Persona("74140221", "cristian", "cruz")

print("Nombre: {}".format(my_person.nombre))
print("Apellido: {}".format(my_person.apellido))
my_person.caminar()
print("Dni de la persona: {}".format(my_person.getDni()))
