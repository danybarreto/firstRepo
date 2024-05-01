# firstRepo

Programa: IMCdbf.py
--
Calcula el indice de masa corporal mediante el peso y la estatura

nombre = input("Por favor ingrese su nombre completo: ")
--
se pide por teclado que el usuario ingrese su nombre completo y se guarda en la variable "nombre"

edad = input("Ingresar edad: ")
--
ingresa la edad, se guarda en la variable "edad"

peso = float(input("Ingresar peso: "))
--
ingresa el peso, se guarda en la variable "peso"

estatura = float(input("Ingresar estatura: "))
--
ingresa la estatura, se guarda en la variable "estatura"

--
imc = peso / estatura ** 2
--
se eleva al 2(cuadrado) la estatura y se divide entre el peso, el resultado se guarda en el variable "imc".

print("Sr/Sra: " + nombre)
--
Se imprime en pantalla el msg Sr/Sra, concatenado con el valor de la variable "nombre"

print("Con una edad de: " + edad + " Años")
--
Se imprime en pantalla el msg Con una edad de: , concatenado con el valor de la variable "edad" y el msg Años

print("Y un peso de: " + str(peso) + " Kilos")
--
Se imprime en pantalla el msg Y un peso de: , concatenado con el valor de la variable "peso" convertida a string y el msg Kilos

print("Estatura de: " + str(estatura))
--
Se imprime en pantalla el msg Estatura de: , concatenado con el valor de la variable "estatura" convertida a string

print("Su IMC es de: " + str(imc))
--
Imprime en pantalla el msg Su IMC es de: concatenado el valor de la variable imc convertida a string
