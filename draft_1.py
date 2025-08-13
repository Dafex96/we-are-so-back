while True:
    try:
        num = int(input("Ingrese un numero: "))
        
        if num > 0:
            print("El numero es positivo")
        elif num < 0:
            print("El numero es negativo")
        elif num == 0:
            print("El numero es 0")
    except ValueError:
        print("Debe ingresar in numero, vuelva a intentearlo")