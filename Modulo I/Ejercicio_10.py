def numero_perfectos(num):
    
    if num < 0:
        print("Tiene que ser un numero positivo")

    acumuladora = 0

    for i in range(1, num):

        if num % i == 0:
            acumuladora += i
    
    if acumuladora == num:
        print("Es perfecto")
    else:
        print("No es perfecto")
    
numero = int(input("Diga el numero para verificar si es perfecto:\n"))
numero_perfectos(numero)