def es_valido(tablero, fila, columna, num):
    # Verificar fila
    if num in tablero[fila]:
        return False
    # Verificar columna
    if num in [tablero[i][columna] for i in range(9)]:
        return False
    # Verificar subcuadrícula 3x3
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == num:
                return False
    return True

def encontrar_vacia(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:  # Celda vacía
                return i, j
    return None

def resolver_sudoku(tablero):
    vacia = encontrar_vacia(tablero)
    if not vacia:  # No hay más celdas vacías
        return True
    fila, columna = vacia

    for num in range(1, 10):  # Intentar números del 1 al 9
        if es_valido(tablero, fila, columna, num):
            tablero[fila][columna] = num  # Colocar número
            if resolver_sudoku(tablero):  # Continuar recursivamente
                return True
            tablero[fila][columna] = 0  # Retroceder

    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

# Ejemplo de tablero incompleto
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Tablero inicial:")
imprimir_tablero(tablero)

while True:
    resolver = input("\n¿Quieres activar el algoritmo para resolver el Sudoku por ti? (sí/no/salir): ").strip().lower()
    if resolver in ["sí", "si"]:
        if resolver_sudoku(tablero):
            print("\nSudoku resuelto:")
            imprimir_tablero(tablero)
        else:
            print("\nNo hay solución para este Sudoku.")
        break  # Salir del bucle tras resolver el Sudoku
    elif resolver in ["no"]:
        print("\nPuedes intentar resolver el Sudoku por ti mismo. Buena suerte!")
    elif resolver in ["salir"]:
        print("\nGracias por jugar. ¡Hasta luego!")
        break
    else:
        print("\nPor favor, responde con 'sí', 'no' o 'salir'.")
