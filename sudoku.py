import os

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
            print(valor if valor != 0 else " ", end=" ")
        
        print()


TABLERO_PREDETERMINADO = [       #modo normal
    [8, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 0],
    [9, 0, 5, 0, 0, 0, 0, 0, 0],
    [3, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [2, 0, 9, 0, 8, 0, 0, 7, 0],
    [0, 9, 0, 8, 0, 0, 6, 0, 2],
    [7, 0, 5, 0, 0, 0, 0, 0, 0]
]

#se usara un tablero fijo y la dificultad estara en su numero de incognitas. Mientras tanto este sera el de modo normal

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
                #y lo coloca
                tablero[fila_idx][col_idx] = numero
                input("\nNumero colocado. Presiona Enter para continuar...")
                
            case "2": #aqui deberia mostrar el juego resuelto
                print("\nTe has rendido. Volviendo al menu principal...")
                input("Presiona Enter para continuar...")
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
        
        #pasar esto a case 
        if opcion == "1": 
            tablero_juego = [fila[:] for fila in TABLERO_PREDETERMINADO]
            jugar_sudoku(tablero_juego)
            
        elif opcion == "2":
            print("\nSaliendo del juego...")
            break
        else:
            print("\nOpcion invalida. Por favor, intente nuevamente.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()

#por hacer:
#ponerle color a los num que no son pistas y a los ingresados por el usuario
#que detecte que los numeros ingresados no se repitan en la columna ni en la fila
#que registre al usuario que este jugando
#mostrar el sudoku resuelto cuando se rinda