nombre = input("Por favor ingrese su nombre completo: ")
edad = input("Ingresar edad: ")
peso = float(input("Ingresar peso: "))
estatura = float(input("Ingresar estatura: "))

imc = peso / estatura ** 2

print("Sr/Sra: " + nombre)
print("Con una edad de: " + edad + " Años")
print("Y un peso de: " + str(peso) + " Kilos")
print("Estatura de: " + str(estatura))
print("Su IMC es de: " + str(imc))
