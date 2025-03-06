import collections
from collections import deque

class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    
    def invertir_lista(self, lista):
        return lista[::-1]

    def buscar_elemento(self, lista, elemento):
        return lista.index(elemento) if elemento in lista else -1

    def eliminar_duplicados(self, lista):
        # Mantener el orden y evitar la conversión de True a 1
        seen = set()
        resultado = []
        for item in lista:
            clave = (type(item), item)  # Diferenciar por tipo y valor
            if clave not in seen:
                seen.add(clave)
                resultado.append(item)
        return resultado

    def merge_ordenado(self, lista1, lista2):
        return sorted(lista1 + lista2)

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        k = k % len(lista)
        return lista[-k:] + lista[:-k]

    def es_subconjunto(self, conjunto1, conjunto2):
        return set(conjunto1).issubset(set(conjunto2))

    def encuentra_numero_faltante(self, numeros):
        n = len(numeros) + 1
        suma_esperada = n * (n + 1) // 2
        suma_actual = sum(numeros)
        return suma_esperada - suma_actual

    class Pila:
     def __init__(self):
        self.items = []

    def is_empty(self): 
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):  # <--- Agregado
        if not self.is_empty():
            return self.items[-1]
        return None


    class Cola:
     def __init__(self):
        self.items = []

     def is_empty(self):
        return len(self.items) == 0

     def enqueue(self, item):
        self.items.append(item)

     def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

     def peek(self):  # <--- Agregado
        if not self.is_empty():
            return self.items[0]
        return None


    def implementar_pila(self):
        return self.Pila()

    def implementar_cola(self):
        return self.Cola()
    def matriz_transpuesta(self, matriz):
        return [list(fila) for fila in zip(*matriz)] if matriz else []
    
    def encuentra_numero_faltante(self, numeros):
        n = len(numeros) + 1
        suma_esperada = n * (n + 1) // 2
        suma_actual = sum(numeros)
        return suma_esperada - suma_actual
