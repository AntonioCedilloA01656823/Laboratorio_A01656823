#Antonio Cedillo, A01656823
#Repaso de conceptos en Python

""" Función que   encuentre los 
números primos de los primeros N números naturales. """
import numpy as np
from pathlib import Path

def esPrimo(num):
    for n in range(2,num):
        if (num%n == 0):
            return False
    return True

def numerosPrimos(N):
    primos = []
    for numero in range (2,N+1): #1 se puede considerar
        primo = esPrimo(numero)


        if (primo == False):
            print("El numero: " + str(numero) + "  NO es primo")
        elif (primo == True):
            primos.append(numero)

    print("Lista de todos los numeros primos: ")
    print(primos)




"""función en Python que calcule 
el producto cruz enn vectores de 3 componentes."""

def productoCruz(vector1,vector2): #checar con profe
    if isinstance(vector1, list) and isinstance(vector2,list):
        #haciendo todos float por si acaso
        v1 = np.array(vector1,float)
        v2 = np.array(vector2,float)

        #forma facil 
        print("el producto cruz de: " + np.array2string(v1) + " y " 
              + np.array2string(v2) + " es: " )
        print(np.cross(v1,v2))
    else:
        print("Algunos de tus elementos no es una lista")


"""función 2 pero ahora con 
vectores que son leidos desde un archivo de texto."""

def pcArchivo(file):
    if (type(file) == str ):
        if(Path(file).suffix == '.csv'):
            archivo = open("vectores.csv","r")
            for line in archivo:
                print(line)
        else:
            print("Ingresa un archivo .csv, por favor")
    
    else: 
        print("Ingresa una variable de string, por favor")
    


def main():
    print("Función numeros primos")
    numerosPrimos(30)
    print("----------")


    print("Función producto cruz lista")
    v1,v2 = [3,4,6],[7,10,8]
    productoCruz(v1,v2)
    print("----------")
    
    print("Función producto cruz archivo")
    pcArchivo("vectores.csv")



main()