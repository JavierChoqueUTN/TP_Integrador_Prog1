#region Listas
alumnos_lista = {
    5: "Arnez",
    2: "Ramirez",
    8: "Choque",
    1: "Gonzalez",
    6: "Gutierrez",
    4: "Lopez",
    9: "Campana",
    3: "Martinez",
    7: "Chiavon"
}

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
    if lista_de_nodos is None:          # Caso base: si la lista está vacía o None, no se hace nada, se retorna al usuario
        return
    
    # Se calculan los espacios y guiones para mostrar la jerarquía visualmente
    espacio_final = "  " * multiplicador_espacios   # Cantidad de espacios de indentación (2 espacios por nivel)
    guion_final = "|_" * multiplicador_guion        # Prefijo con guiones para marcar subniveles (aparece solo a partir del segundo nivel)
    identacion = espacio_final + guion_final        # Se combina la indentación total
    
    print(f"{identacion}{lista_de_nodos[0]}")       # Se imprime el nombre del nodo actual (la posición 0 de la lista)
    
    # Llamada recursiva para el hijo izquierdo
    if len(lista_de_nodos) > 1 and lista_de_nodos[1] != []:   # Se verifica si existe un hijo izquierdo (posición 1) y no está vacío
        imprimir_arbol(lista_de_nodos[1] , multiplicador_espacios + 1, multiplicador_guion=1) # Se llama recursivamente a la función con el hijo izquierdo
    
    # Llamada recursiva para el hijo derecho
    if len(lista_de_nodos) > 2 and lista_de_nodos[2] != []:  # Se verifica si existe un hijo derecho (posición 2) y no está vacío
        imprimir_arbol(lista_de_nodos[2], multiplicador_espacios + 1, multiplicador_guion=1) # Se llama recursivamente a la función con el hijo derecho

def buscar_elemento(lista_de_nodos, valor_buscado, camino=None):
    if camino is None:
        camino = []

    valor_primera_pos = lista_de_nodos[0]
    camino_actual = camino + [valor_primera_pos] # Se hace una copia de "camino" para no afectar la recursividad. A la lista vacía, se le agrega el valor
#                                                 del elemento en la primera posición de la "lista_de_nodos".      
    if valor_primera_pos == valor_buscado:
        return camino_actual                     # Si el valor en el primer recorrido es igual al objetivo buscado, se sale de la función retornando la lista acumulada "camino_actual". 

    for i in range(1, len(lista_de_nodos)):      # Se recorre "lista_de_nodos" a partir de posición 1. Es decir, solo pos 1 y 2.
        hijo = lista_de_nodos[i]                 # Se considera a cada uno de los elementos de la "lista_de_nodos" como un "hijo" de la misma.
        if hijo == []:                           # En caso de que al recorrer se encuentre un elemento vacío, este se saltea con continue.
            continue

        camino_actual_rec = buscar_elemento(hijo, valor_buscado, camino_actual)
        # Se vuelve a ejecutar la función recursivamente. En caso de que se encuentre,
        # la variable "camino_actual_rec" almacenará el camino acumulado en la recursividad hasta llegar al elemento buscado.                                                                        
        if camino_actual_rec is not None:    # Si "camino_actual_rec" almacenó correctamente los valores, estos serán retornados al usuario.
            return camino_actual_rec

    return None                              # En caso de que no se haya encontrado al "valor_buscado", entonces se retornara "None" al usuario.

def busqueda_lineal(id_buscado):
    tiempo_inicial = time.time()
    for clave, valor in alumnos_lista.items():
        if clave == id_buscado:
            tiempo_final = time.time()
            duracion_busqueda_lineal = (tiempo_final - tiempo_inicial) * 1000
            return valor, duracion_busqueda_lineal
    return None, None

def busqueda_binaria(id_buscado):
    # Convertimos a una lista de tuplas ordenadas por clave
    items_ordenados = sorted(alumnos_lista.items())  # [(1, "Gonzalez"), (2, "Ramirez"), ...]
    izquierda = 0
    derecha = len(items_ordenados) - 1

    tiempo_inicial = time.time()
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        clave_medio, valor_medio = items_ordenados[medio]

        if clave_medio == id_buscado:
            tiempo_final = time.time()
            duracion_busqueda_binaria = (tiempo_final - tiempo_inicial) * 1000
            return valor_medio, duracion_busqueda_binaria
        elif id_buscado < clave_medio:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return None, None

def recorrido_inorden(lista_de_nodos):
    """
    Recorre el árbol en orden (in-orden): hijo izquierdo -> raíz -> hijo derecho.
    Útil para estructuras binarias cuando se quiere un recorrido ordenado.
    """
    if lista_de_nodos is None or lista_de_nodos == []:
        return

    if len(lista_de_nodos) > 1:
        recorrido_inorden(lista_de_nodos[1])  # Recorre hijo izquierdo

    print(lista_de_nodos[0])                  # Visita la raíz (nodo actual)

    if len(lista_de_nodos) > 2:
        recorrido_inorden(lista_de_nodos[2])  # Recorre hijo derecho

def recorrido_preorden(lista_de_nodos):
    """
    Recorre el árbol en pre-orden: raíz -> hijo izquierdo -> hijo derecho.
    Útil para clonar o copiar la estructura del árbol.
    """
    if lista_de_nodos is None or lista_de_nodos == []:
        return

    print(lista_de_nodos[0])                  # Visita la raíz (nodo actual)

    if len(lista_de_nodos) > 1:
        recorrido_preorden(lista_de_nodos[1]) # Recorre hijo izquierdo

    if len(lista_de_nodos) > 2:
        recorrido_preorden(lista_de_nodos[2]) # Recorre hijo derecho

def recorrido_postorden(lista_de_nodos):
    """
    Recorre el árbol en post-orden: hijo izquierdo -> hijo derecho -> raíz.
    Útil para eliminar o evaluar estructuras completas desde las hojas hacia la raíz.
    """
    if lista_de_nodos is None or lista_de_nodos == []:
        return

    if len(lista_de_nodos) > 1:
        recorrido_postorden(lista_de_nodos[1]) # Recorre hijo izquierdo

    if len(lista_de_nodos) > 2:
        recorrido_postorden(lista_de_nodos[2]) # Recorre hijo derecho

    print(lista_de_nodos[0])                   # Visita la raíz (nodo actual)

#endregion

#region Programa Principal
print("Bienvenido profesor. Por favor, ingrese la acción que desea realizar:")
print("1. Ver jerarquía total de aulas. \n2. Buscar elemento y ver su profundidad. \n3. Buscar alumno. \n4. Recorridos del árbol (in-orden, pre-orden, post-orden).\n0. Salir.")
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
            nodos = len(camino_elemento_a_origen)
            profundidad = len(camino_elemento_a_origen) - 1
            nivel = profundidad + 1
            print(f"Camino es: {camino_elemento_a_origen}.")
            print(f"Nodos incluidos:{nodos} ")
            print(f"Profundidad: {profundidad}")
            print(f"Nivel: {nivel}")
#            print(f"\nOpción {opcion} completada. Hasta luego!")
        else:
            print("No se encontró elemento.")
#            print(f"\nOpción {opcion} completada. Hasta luego!")
        break

    elif (opcion == "3"):
        limpiar_pantalla()
        id_buscado = int(input("Ingrese ID del alumno a buscar:"))
        apellido_encontrado, duracion_busqueda_lineal = busqueda_lineal(id_buscado)
        apellido_encontrado, duracion_busqueda_binaria = busqueda_binaria(id_buscado)
        if apellido_encontrado is not None:
            print(f"ID : {id_buscado} corresponde a alumno {apellido_encontrado}.")
            print(f"Duración realizando busqueda lineal: {duracion_busqueda_lineal} milisegundos.")
            print(f"Duración realizando busqueda binaria: {duracion_busqueda_binaria} milisegundos.")
        else:
            print("No existe el ID de alumno ingresado en la base de datos.")
        break
    elif (opcion == "4"):
        limpiar_pantalla()
        print("Recorrido in-orden:")
        recorrido_inorden(provincia_lista)
        print("\nRecorrido pre-orden:")
        recorrido_preorden(provincia_lista)
        print("\nRecorrido post-orden:")
        recorrido_postorden(provincia_lista)
        break
    elif (opcion == "0"):
        continue
    else:
        limpiar_pantalla()
        print("Ingrese una opción válida.")
        print("1. Ver jerarquía total de aulas. \n2. Buscar elemento y ver su profundidad. \n3. Buscar alumno.\n0. Salir.")
print(f"\nOpción {opcion} completada. Hasta luego!\n")
#endregion