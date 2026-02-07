print("Bienvendos al centro comercial")
metodo_pago = input(("Ingrese cual sera su metodo de pago\n"
                "1. Pago movil \n"
                "2. Tarjeta \n"))

if metodo_pago in ["1","2"]:
    if metodo_pago == "1":
        clave = input("Ingrese la clave de 8 digitos:\n")
        verificacion = clave.isdigit()
        cantidad_pago = len(clave)
        if len(clave) == 8 and verificacion:
            print("Gracias por tu pago, fue verificado")
        else: print("Error...La clave es de 8 digitos")
    elif metodo_pago == "2":
        clave = input("Ingrese la clave de 16 digitos:\n")
        verificacion = clave.isdigit()
        if clave(len)== 16 and verificacion:
            print("Gracias tu tarjeta fue aprobada...")
        else: print("Error...La clave es de 16 digitos")
    else: "Opcion no valida"