import random

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Función para crear un tablero vacío
def crear_tablero(filas, columnas):
    return [["~" for _ in range(columnas)] for _ in range(filas)]

# Función para colocar barcos en el tablero
def colocar_barcos(tablero, num_barcos):
    filas = len(tablero)
    columnas = len(tablero[0])
    for _ in range(num_barcos):
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        while tablero[fila][columna] == "O":
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
        tablero[fila][columna] = "O"

# Función para el turno del jugador
def turno_jugador(tablero):
    fila = int(input("Ingresa la fila para atacar: "))
    columna = int(input("Ingresa la columna para atacar: "))
    if tablero[fila][columna] == "O":
        print("¡Impacto! Hundiste un barco.")
        tablero[fila][columna] = "X"
    else:
        print("Agua. No impactaste ningún barco.")

# Función para el turno de la computadora
def turno_computadora(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    fila = random.randint(0, filas - 1)
    columna = random.randint(0, columnas - 1)
    if tablero[fila][columna] == "O":
        print("¡La computadora impactó un barco tuyo!")
        tablero[fila][columna] = "X"
    else:
        print("La computadora atacó en", fila, ",", columna, ". No impactó ningún barco tuyo.")

# Función para verificar si todos los barcos han sido hundidos
def todos_barcos_hundidos(tablero):
    for fila in tablero:
        if "O" in fila:
            return False
    return True

# Función principal del juego
def jugar_batalla_naval(filas, columnas, num_barcos):
    print("¡Bienvenido a Batalla Naval!")
    tablero_jugador = crear_tablero(filas, columnas)
    tablero_computadora = crear_tablero(filas, columnas)
    colocar_barcos(tablero_jugador, num_barcos)
    colocar_barcos(tablero_computadora, num_barcos)
    
    while True:
        print("\nTablero del Jugador:")
        imprimir_tablero(tablero_jugador)
        print("\nTablero de la Computadora:")
        imprimir_tablero(tablero_computadora)
        
        turno_jugador(tablero_computadora)
        if todos_barcos_hundidos(tablero_computadora):
            print("¡Felicidades! Has ganado.")
            break
        
        turno_computadora(tablero_jugador)
        if todos_barcos_hundidos(tablero_jugador):
            print("¡La computadora ha ganado! Mejor suerte la próxima vez.")
            break

# Ejecutar el juego
jugar_batalla_naval(5, 5, 5)
