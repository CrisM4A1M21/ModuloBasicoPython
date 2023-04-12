class A:
    def __init__(self):
        self.inicial = False
        self._contador = 0  # Atributo privado pero modificable

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador


class B:
    def __init__(self):
        self.inicial = True
        self.__contador = 0  # Atributo privado pero no modificable

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

print("Clase A")
varA = A()
varA._contador = 5

varA.inicial = True
varA.incrementa()
varA.incrementa()

print(varA.cuenta())

print("Clase B")
varB = B()
varB.__contador = 5

varB.inicial = True
varB.incrementa()
varB.incrementa()

print(varB.cuenta())