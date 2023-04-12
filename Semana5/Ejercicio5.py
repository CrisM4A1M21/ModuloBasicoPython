def operacion(a, b):
    try:
        resultado = a + b
        return print(resultado)
    except (TypeError, ZeroDivisionError):
        print("Exception TypeError/ZeroDivisionError")
    else:
        print(resultado)
        
operacion(4, 6)