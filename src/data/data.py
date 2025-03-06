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

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_total = n * (n - 1) // 2  # Fórmula correcta para la suma esperada
        suma_lista = sum(lista)
        return suma_total - suma_lista

    def es_subconjunto(self, conjunto1, conjunto2):
        return set(conjunto1).issubset(set(conjunto2))

    def implementar_pila(self):
        class Pila:
            def __init__(self):
                self.items = []

            def push(self, item):
                self.items.append(item)

            def pop(self):
                return self.items.pop() if self.items else None

            def is_empty(self):
                return not self.items
        
            def size(self):
                return len(self.items)
        
        return Pila()

    def implementar_cola(self):
        class Cola:
            def __init__(self):
                self.items = collections.deque()

            def enqueue(self, item):
                self.items.append(item)

            def dequeue(self):
                return self.items.popleft() if self.items else None

            def is_empty(self):
                return not self.items
        
            def size(self):
                return len(self.items)
        
        return Cola()

    def matriz_transpuesta(self, matriz):
        return [list(fila) for fila in zip(*matriz)] if matriz else []
