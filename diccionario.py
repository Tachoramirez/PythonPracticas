"""
Nombre: Diccionario.py
Objetivo: Muestra la operación de los diccionarios en Python
Autor: El Tacho
Fecha: 05/08/2020
"""

#Diccionario es una estructura de datos que almacena valores heterogeneos
#los almacena en un formato de clave:valor. Quiere decir que cada elemento
#en el diccionario se almacena como una lista de pares Key:valor
#Ejemplo: 'nombre':'Tacho'
#No son mutables, osea, no cambian. Una vez que los creamos permanecerán
#con los mismos valores, no podremos introducir mas datos


def main():
    #Creamos diccionario con distintos key y datos
    dic = {'clave':16460686, 'nombre':'El tacho', 'edad':25, 'cursos':['Python', 'Progra Web', 'Inteligencia Web']}
    #listar items del diccionario
    print("Los items son: ",dic)
    #Imprimir un elemento de un diccionario
    print("El valor de la key es: ",dic['nombre'])
    #Imprimir los valores de los keys del diccionario
    for i in dic:
        print(i,":",dic[i])

    #En el caso de la lista incluida como un item del diccionario, lo accesamos
    print("\n")
    for i in dic['cursos']:
        print(i)

    #Investigar los metodos de los diccionarios
    #get, pop, key, clean, items, update

    print("=================================== TAREA ==================================")
    print("============================================================================")

    print("=========== GET() ================\n")
    """
    === GET() ===
    Recibe como parámetro una clave, devuelve el valor de la clave. 
    Si no lo encuentra, devuelve un objeto none.
    """
    vGet = dic.get('sope')
    print("Resultado de GET es: ",vGet,"\n")
    print("==================================\n")

    print("=========== POP() ================\n")
    """
    === POP() ===
    Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.
    """
    vPop = dic.pop('edad')
    print("Resultado de POP es: ",vPop)
    print("Los items después de apilcar POP('edad') son: ",dic,"\n")    
    print("==================================")

    #Definimos nuevo Diccionario para pruebas con una variable.
    dic1 = {'a':1, 'b':2, 'c':3}
    print("Diccionario1: ",dic1)

    print("=========== FROMKEYS() =============\n")
    """
    Recibe como parámetros un iterable y un valor, 
    devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado. 
    Si el valor no es ingresado, devolverá none para todas las claves.
    """
    dic1 = dic1.fromkeys(['a','b','c'],2020)
    print("Diccionario1: ",dic1)
    print("=====================================\n")
    print("=========== ITEMS() ==================\n")
    """
    Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
    """
    items = dic1.items()
    print(items)
    print("========================================\n")
    print("=========== CLEAR() ================\n")
    """
    === CLEAR() ===
    Elimina todos los ítems del diccionario dejándolo vacío. 
    """
    print("Diccionario1 antes de CLEAR: ",dic1)
    dic1.clear()
    print("Diccionario1 después de CLEAR: ",dic1)
    print("==================================\n")


    print("=========== UPDATE() ================\n")
    """
    === UPDATE() ===
    Recibe como parámetro otro diccionario. 
    Si se tienen claves iguales, actualiza el valor de la clave repetida; si no hay claves iguales, 
    este par clave-valor es agregado al diccionario.
    """
    print("Primer diccionario creado en el archivo: ",dic)
    dic2 = {'a':4, 'b':5, 'c':6}
    dic.update(dic2)
    print("Resultado de UPDATE: ",dic,"\n")
    print("==================================\n")


if __name__ == "__main__":
    main()