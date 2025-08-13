# IMC = peso(kg) / (altura (m))al cuadrao

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su estatura: "))

imc = peso / altura ** 2

print(f"Su imc es: {imc}")