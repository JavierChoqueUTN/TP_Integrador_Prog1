#region Listas
aula1_lista = ["Aula 1", [], []]
aula2_lista = ["Aula 2", [], []]
aula3_lista = ["Aula 3", [], []]
aula4_lista = ["Aula 4", [], []]
aula5_lista = ["Aula 5", [], []]
aula6_lista = ["Aula 6", [], []]
aula7_lista = ["Aula 7", [], []]
aula8_lista = ["Aula 8", [], []]

escuela1_lista = ["Escuela 1", aula1_lista, aula2_lista]
escuela2_lista = ["Escuela 2", aula3_lista, aula4_lista]
escuela3_lista = ["Escuela 3", aula5_lista, aula6_lista]
escuela4_lista = ["Escuela 4", aula7_lista, aula8_lista]

distrito1_lista = ["Distrito 1", escuela1_lista, escuela2_lista]
distrito2_lista = ["Distrito 2", escuela3_lista, escuela4_lista]

provincia_lista = ["Neuquen", distrito1_lista, distrito2_lista]
#endregion

#region funciones auxiliares
import os
import time
def limpiar_pantalla():
    os.system("cls")

#endregion

#region funciones principales
def imprimir_arbol(lista_de_nodos, multiplicador_espacios=0, multiplicador_guion=0):
    """Imprime el árbol de forma simple con indentación"""
    if lista_de_nodos is None: #Si la "lista_de_nodos" está vacía, entonces se retorna al usuario. 
        return
    espacio_final = "  " * multiplicador_espacios
    guion_final = "|_" * multiplicador_guion
    identacion = espacio_final + guion_final
    
    print(f"{identacion}{lista_de_nodos[0]}") #Se imprime el valor del nodo actual
    
    # Llamada recursiva para el hijo izquierdo
    if len(lista_de_nodos) > 1 and lista_de_nodos[1] != []:
        imprimir_arbol(lista_de_nodos[1] , multiplicador_espacios + 1, multiplicador_guion=1)
    
    # Llamada recursiva para el hijo derecho
    if len(lista_de_nodos) > 2 and lista_de_nodos[2] != []:
        imprimir_arbol(lista_de_nodos[2], multiplicador_espacios + 1, multiplicador_guion=1)

def buscar_elemento(lista_de_nodos, valor_buscado, camino=None):
    if camino is None:
        camino = []

    valor_primera_pos = lista_de_nodos[0]
    camino_actual = camino + [valor_primera_pos] #Se hace una copia de "camino" para no afectar la recursividad. A la lista vacía, se le agrega el valor
#                                                 del elemento en la primera posición de la "lista_de_nodos".      
    if valor_primera_pos == valor_buscado:
        return camino_actual #Si el valor en el primer recorrido es igual al objetivo buscado, se sale de la función retornando la lista acumulada "camino_actual". 

    for i in range(1, len(lista_de_nodos)): #Se recorre "lista_de_nodos" a partir de posición 1. Es decir, solo pos 1 y 2.
        hijo = lista_de_nodos[i]  #Se considera a cada uno de los elementos de la "lista_de_nodos" como un "hijo" de la misma.
        if hijo == []: #En caso de que al recorrer se encuentre un elemento vacío, este se saltea con continue.
            continue

        camino_actual_rec = buscar_elemento(hijo, valor_buscado, camino_actual) #Se vuelve a ejecutar la función recursivamente. En caso de que se encuentre,
#                                                                               la variable "camino_actual_rec" almacenará el camino acumulado en la recursividad hasta llegar al elemento buscado.                                                                        
        if camino_actual_rec[0] is not None:    #Si "camino_actual_rec" almacenó correctamente los valores, estos serán retornados al usuario.
            return camino_actual_rec

    return None #En caso de que no se haya encontrado al "valor_buscado", entonces se retornara "None" al usuario.

#endregion

#region Programa Principal
print("Bienvenido profesor. Por favor, ingrese la acción que desea realizar:")
print("1. Ver jerarquía total de aulas. \n2. Buscar elemento y ver su profundidad. \n3. Ingresar alumnos a un aula existente.\n0. Salir.")
opcion = -1 #Inicializo variable para que el while arranque
while opcion != "0":
    opcion = input() 
    if (opcion == "1"): 
        limpiar_pantalla()
        print("Debajo se encuentra la jerarquía total de aulas.")
        imprimir_arbol(provincia_lista)
        break
    elif (opcion == "2"):
        limpiar_pantalla()
        elemento_buscado = input("Ingrese elemento que desea buscar:")
        camino_elemento_a_origen = buscar_elemento(provincia_lista, elemento_buscado)
        if camino_elemento_a_origen is not None:
            profundidad = len(camino_elemento_a_origen) - 1
            nivel = profundidad + 1
            print(f"Camino es: {camino_elemento_a_origen}.")
            print(f"Profundidad es: {profundidad}")
        else:
            print("No se encontró elemento.")
        break
    else:
        limpiar_pantalla()
        print("Ingrese una opción válida.")
        print("1. Ver jerarquía total de aulas. \n2. Buscar elemento y ver su profundidad. \n3. Ingresar alumnos a un aula existente.")

#endregion

