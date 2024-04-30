def calcular_imc(peso, estatura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos y la estatura en metros.
    """
    return peso / (estatura ** 2)

def main():
    # Solicitar al usuario que ingrese sus datos
    nombre = input("Ingresa tu nombre: ")
    apellido_paterno = input("Ingresa tu apellido paterno: ")
    apellido_materno = input("Ingresa tu apellido materno: ")
    edad = int(input("Ingresa tu edad: "))
    peso = float(input("Ingresa tu peso en kilogramos: "))
    estatura = float(input("Ingresa tu estatura en metros: "))

    # Calcular el IMC
    imc = calcular_imc(peso, estatura)

    # Mostrar los datos junto con el IMC
    print("\nDatos personales:")
    print("Nombre completo:", nombre, apellido_paterno, apellido_materno)
    print("Edad:", edad, "años")
    print("Peso:", peso, "kg")
    print("Estatura:", estatura, "m")
    print("Índice de Masa Corporal (IMC):", imc)

if __name__ == "__main__":
    main()
