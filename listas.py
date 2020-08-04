"""
Nombre: listas
Autor: ElTacho
Objetivo: Muestra el funcionamiento de las listas en python
"""

def main():
    #una lista es una estructura de datos
    #La ventaja aceptan datos de tipos distintos
    #Creamos Listas
    lista = [1, 23.01, False, "hola lista", "A", [-1, -5, "hola", 0.0],-12, "A"]
    #Lista vacia
    listaVacia = []
    #Accesando elementos de lista
    for elemento in lista:
        print ("El elemeno de la lista es: ", elemento)

    for i in listaVacia:
        print("El elemento de la lista es: ", i)

    #Imprimir un elemento de la lista
    print("Elemento en la posición 3: ",lista[3])
    print("Elemento en la posición -5: ",lista[-5])
    print(lista[-2])
    print(lista[5])
    #leer el elemento que está en la posición 2 de la lista interna
    print(lista[5][2])

    # Métodos de las listas:
    # Append, agrega elemento al final de la lista
    lista.append("El maestro no sabe...")
    for elemento in lista:
        print ("El elemeno de la lista es: ", elemento)
    #Count regresa el número de veces que se repite un elemento en la lista
    print("los elementos: ",lista.count("A"))
    #index() imprime el índice de un elemento de la lista
    print(lista.index("hola lista"))
    #remove(), elimina elementos de la lista
    lista.remove("hola lista")
    for x in lista:
        print ("El elemeno de la lista es: ", x)

if __name__=="__main__":
    main()