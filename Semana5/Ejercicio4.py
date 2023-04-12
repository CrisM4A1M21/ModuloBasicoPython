def operaciones(a, b):
    try:
        resultado = a + b
    except TypeError:
        print("Ambos valores tienen que ser de tipo numerico")
    else:
        print(resultado)

operaciones(6, 9)
operaciones(6, "fdsafds")
operaciones("dsffsa", 9)

def operaciones1(a, b):
    try:
        resultado = int(a) + int(b)
    except TypeError:
        print("Ambos valores tienen que ser de tipo numerico")
    except ValueError:
        print("Ambos valores tienen que ser de tipo numerico")
    else:
        print(resultado)

operaciones1("ada",5)

a = 5

if type(a) == int:
    print("a es un numero")
else:
    print("es otra cosa")