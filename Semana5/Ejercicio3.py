try:
    var = 100/0

except TypeError:
    print("Tipo de dato ingresado incorrecto")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except IndexError:
    print(IndexError)
except KeyError:
    print("Esta llave no existe en el diccionario")
except FileNotFoundError:
    print("No existe el archivo en la ruta especificada")
except ImportError:
    print("No existe la libreria")

def division(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except TypeError:
        print("No son numeros los datos ingresados")

division(9, 0)
division(9, "VFDSf")
division(9, 3)
