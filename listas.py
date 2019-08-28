#!/usr/bin/python3

def listas():
    while True:
        #os.system('cls')
        print("\n\tLISTAS")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("salir")
        user_input = input(" :")
        if user_input == "salir":
            break
        elif user_input == "1":
            while True:
                print("\n\tBloque de ejercicios de ejercicio #1")
                print("1). BLOQUE")
                print("2). BLOQUE")
                print("3). BLOQUE")
                print("salir")
                user_input = input(" :")
                if user_input == "salir":
                    break
                elif user_input == "1":
                    print("\n")
                elif user_input == "2":
                    print("\n")
                elif user_input == "3":
                    print("\n")
                else :
                    print("\n")

        #mas opciones abajo
        else:
            print("\n")
