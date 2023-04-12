class Perro():
    def sonido(self):
        print("Guau")


class Gato():
    def sonido(self):
        print("Miau")


class Vaca():
    def sonido(self):
        print("Muuuu")


gato = Gato()
perro = Perro()
vaca = Vaca()

lista = [gato, perro, vaca]

def canto(animales):
    for i in animales:
        i.sonido()

canto(lista)