eleccion = input("Eliga el tipo de vehiculo que desee \n"
                 "Pickup (6.00$) \n" 
                 "Gandola (7.00$)\n"
                 "Mudanza (10.00$)\n").lower()

if eleccion in ["pickup", "gandola", "mudanza"]:
    kilometros = float(input("Cuantos Kilometros desea desplazarse:\n"))
    cargo = kilometros
    match eleccion:
        case "pickup":
            precio_estandar = 6.00
        case "gandola":
            precio_estandar = 7.00
        case "mudanza":
            precio_estandar = 10.00
    
    cargo_kilometraje = kilometros * 1.50
    total = precio_estandar + cargo_kilometraje

    print("\n--- REPORTE FINAL ---")
    print(f"Precio base: ${precio_estandar}")
    print(f"Costo por distancia ({kilometros} km): ${cargo_kilometraje}")
    print(f"Monto total facturado: ${total}")
else: print("Opcion invalida")