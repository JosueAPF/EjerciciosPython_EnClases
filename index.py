#!/usr/bin/pyrhon3
# -*- coding: utf-8 -*-
import listas
import tuplas
import diccionario
from  colorama import init,Fore,Back,Styl

while True:
    init()
    print(Fore.GREEN+"")
    print("1). listas")
    print("2). tupla")
    print("3). diccionario")
    print("salir")
    print(Fore.WHITE+"\n")
    user_input = input(" :")
    if user_input == "salir":
        break
    elif user_input == "1":
        print(Fore.LIGHTYELLOW_EX+"")
        listas.listas()
        print("\n")
    elif user_input == "2":
        tuplas.tuplas()
        print("\n")
    elif user_input == "3":
        diccionario.diccionario()
        print("\n")
        
    else:
        print("")
    



