import os
import random

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_tablero(tablero):
    print("   1 2 3   4 5 6   7 8 9")
    print("   ---------------------")
    for i, fila in enumerate(tablero): 
        if i % 3 == 0 and i != 0:
            print("   ------+-------+------")
        print(f"{i+1}  ", end="")
        for j, valor in enumerate(fila):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            #el 0 representa los esapacios vacios entonces queremos que se muestre " " un espacio vacio para que sea intuitivo para el usuario
            if valor == 0:
                cell_str = " "
            else:
                if TABLERO_PREDETERMINADO[i][j] != 0:
                    cell_str = f"\033[34m{valor}\033[0m"  #azul
                else:
                    cell_str = f"\033[37m{valor}\033[0m"  #blanco 
            print(cell_str, end=" ")
        print()

def movimiento_valido(tablero, fila_idx, col_idx, numero):
    for c in range(9): #comprueba que en la FILA no este el mismo num
        if tablero[fila_idx][c] == numero:
            return False
    for r in range(9): #comprueba que en la COLUMNA no este el mismo num
        if tablero[r][col_idx] == numero:
            return False
    return True 

def verificar_ganador(tablero, solucion):
    return tablero == solucion #retorna true si las filas en tablero y solucion son iguales

def tablero_con_pistas(tablero_resuelto, num_pistas=1):
    
    num_pistas = max(1, num_pistas)  #garantiza que las pistas no sean 0 o negativo, por default esta en 1, pero por el parametro esta en 80

    
    tablero_copiado_con_pistas = [fila[:] for fila in tablero_resuelto] #[fila[:] for fila va a copiar cada fila de tablero resuelto y lo hara parte de tablero_copiado_con_pistas
    
    posiciones = [(r, c) for r in range(9) for c in range(9)] #luego le coloca las posiciones (r y c) es como (i y j) osea, (0, 0) (0, 1) (0, 2) etc
    random.shuffle(posiciones) #ya que esten registradas esas pociones, las revuelve

    pistas_pos = posiciones[:num_pistas] #si por ejemplo son 2 pistas entonces se queda en  (3,4), (7,1), (1,6), (5,3), (2,8) 
    for r in range(9):
        for c in range(9): #recorre el i j del tablero
            if (r, c) not in pistas_pos: # al recorrer el tablero, todo lo que no sea pistas_pos le pone un 0, haciendolo vacio
                tablero_copiado_con_pistas[r][c] = 0
    return tablero_copiado_con_pistas

TABLERO_PREDETERMINADO = [       #modo normal
    [9, 7, 6, 8, 2, 3, 4, 1, 5],
    [1, 3, 5, 9, 6, 4, 7, 2, 8],
    [8, 2, 4, 7, 5, 1, 9, 6, 3],
    [6, 9, 3, 5, 1, 7, 8, 4, 2],
    [5, 4, 2, 6, 9, 8, 1, 3, 7],
    [7, 8, 1, 3, 4, 2, 6, 5, 9],
    [3, 5, 9, 8, 4, 6, 2, 7, 1],
    [4, 1, 8, 2, 7, 5, 3, 9, 6],
    [2, 6, 7, 1, 3, 9, 5, 8, 4]
]

def jugar_sudoku(tablero):
    while True:
        limpiar_pantalla()
        imprimir_tablero(tablero)
        
        print("\nSeleccione una opcion:")
        print("1. Jugar.")
        print("2. Rendirse.")
        print("3. Salir.")
        opcion_juego = input("Ingrese su opcion: ")
        
        match opcion_juego:
            case "1":
                print("\nIngrese la posicion donde desea colocar un numero:")
                fila = input("Fila (1-9): ")
                columna = input("Columna (1-9): ")
                numero = input("Numero (1-9): ")
                
                #para esta parte suceden 3 pasos:
                #1.valida que las 3 entradas en fila, columna y numero sean numeros. es decir si metes "1" lo pasa a 1. si no, le salta el input
                try:
                    fila = int(fila)
                    columna = int(columna)
                    numero = int(numero)
                except ValueError:
                    input("\nEntrada invalida. Presiona Enter para continuar...")
                    continue
                
                #2. valida que el usuario ingreso numeros 1< o >10. si no, igual le salta el input
                if not (1 <= fila <= 9 and 1 <= columna <= 9 and 1 <= numero <= 9):
                    input("\nFila, columna o numero fuera de rango. Presiona Enter para continuar...")
                    continue
                # a los num ingresados debe restarles uno porque el arreglo del sudoku va desde 0 a 8 
                fila_idx = fila - 1
                col_idx = columna - 1
                
                #3. verifica que la casilla esta vacia
                if tablero[fila_idx][col_idx] != 0:
                    input("\nLa casilla ya contiene un numero. Presiona Enter para continuar...")
                    continue        

                #AÑADIDO el validador de movimientos validos (verifica si el num ingresado en fila y columna)
                if not movimiento_valido(tablero, fila_idx, col_idx, numero):
                    input("\nMovimiento invalido: El numero ya existe en la fila o columna. Presiona Enter para continuar...")
                    continue

                #y lo coloca
                tablero[fila_idx][col_idx] = numero
                input("\nNumero colocado. Presiona Enter para continuar...")
                
                #POR ULTIMO, cada que se añade un numero se llama esta funcion, para ver si el juego esta completado si verificas_ganador devuelva true
                if verificar_ganador(tablero, TABLERO_PREDETERMINADO):
                    limpiar_pantalla()
                    imprimir_tablero(tablero)
                    print("\nFelicidades, ganaste!")
                    input("\nPresiona Enter para salir...")
                    exit()
                
            case "2":
                print("\nTe has rendido. El sudoku resuelto es:")
                imprimir_tablero(TABLERO_PREDETERMINADO)
                input("\nPresiona Enter para continuar...")
                break
            
            case "3":
                print("\nSaliendo del juego...")
                exit()
            
            case _:
                input("\nOpcion invalida. Presiona Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        print("\nBienvenido a Sudoku")
        print("Presione una opcion para continuar:")
        print("1. Jugar")
        print("2. Salir")
        
        opcion = input("Ingrese su opcion (1 o 2): ")
        
        match opcion:
            case "1":
                #genera la copia del tablero, pero con pistas
                #la dificultad es la cantidad de pistas que hay, cambiar el parametro num_pistas
                tablero_juego = tablero_con_pistas(TABLERO_PREDETERMINADO, num_pistas=80) 
                jugar_sudoku(tablero_juego)
            case "2":
                print("\nSaliendo del juego...")
                break
            case _:
                print("\nOpcion invalida. Por favor, intente nuevamente.")
                input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()

#por hacer:
#que registre el nombre del usuario y lo muestre en el tablero de juego y al ganar