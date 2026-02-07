id_unico = int(input("Ingrese el ID del usuario:\n"))

if id_unico % 2 == 0:
    print("Servidor A")
elif not id_unico % 2 == 0:
    print("Servidor B")
else: "Error... Id no valido"