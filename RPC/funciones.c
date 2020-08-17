/**
Nombre: Funciones.c
Objetivo: Muestra las funciones en ansi c
Autor: El Tacho
Fecha: 06/08/2020
**/

#include <stdio.h>

/**
Función para regresar un mensaje
**/

char* getMessage(){
    return "hola mundo";
}

int suma(int n1, int n2){
    return n1+n2;
}

int resta(int n1, int n2){
    return n1-n2;
}

int main(){
    printf("El mensaje es: %s\n",getMessage());
    printf("La suma es: %d\n",suma(8,3));
    printf("La resta es: %d\n",resta(8,3));

    return 0;
}