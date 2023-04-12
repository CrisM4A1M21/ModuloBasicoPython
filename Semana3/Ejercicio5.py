edad = int(input("Cual es su edad?: "))

if 0 < edad < 18:
    print("Usted es menor de edad")
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif edad < 0 or edad >140:
    print("Ingrese una edad valida")
else:
    print("Usted es una persona de la tercera edad")