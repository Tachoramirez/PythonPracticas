"""
Nombre: CudListats.py
Objetivo: implementa las funciones CRUD en una lista
Autor: El Tacho
Fecha: 04/08/2020
"""
import os
#Declaramos una lista global
lista = []

def addElement():
    e = input("---- Ingresa elemento: ")
    lista.append(e)
    print("------- Elemento agregado al cien.--------")
    print("==============================")


def getElement():
    e = input("--- Buscar elemento: ")
    print("Elemento en índice ",lista.index(e))
    print("==============================")


def modifyElement():
    e = input("--- Elemento a modificar: ")
    ind = lista.index(e)
    lista.remove(e)
    d = input("--- Elemento nuevo: ")
    lista.insert(ind,d)
    print("Elemento modificado al cien.")
    print("==============================")
    
def delElement():
    e = input("--- Elemento a eliminar: ")
    lista.remove(e)
    print("--- Elemento eliminado correctamente.")
    print("==============================")

#imprimir los elementos de la lista
def printElements():
    for i in lista:
        print("La lista es: ", i, "\n")

def dashboard():
    os.system('clear')
    opc = 0
    while (opc != 6):
        print("== Operaciones CRUD con lista en Python == ")
        print("1.Agregar elementos")
        print("2.Buscar elementos")
        print("3.Modificar elementos")
        print("4.Eliminar elementos")
        print("5.Imprimir todos los elementos")
        print("6.Salir")
        opc = int(input("Elija una opción entre 1 y 6: \n"))
        if  opc == 1:
            addElement()
        if opc == 2:
            getElement()
        if opc == 3:
            modifyElement()
        if opc == 4:
            delElement()
        if opc == 5:
            printElements()
        if opc == 6:
            print("==============================")
            print("Hasta la vista baby!")
    



def main():
    dashboard()

if __name__ == "__main__":
    main()