caracter_usuario = input("Ingrese un caracter para verificar si es un vocal: \n").lower()

verificacion = len(caracter_usuario)

if verificacion == 1:
    if caracter_usuario in ["a","e","i","o","u"]:
        print(f"Tu caracter es una vocal")
    else: print("Tu caracter no es una vocal")
else: print("No puede ser mas de un caracter")