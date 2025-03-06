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
        return list(dict.fromkeys(lista))

    def merge_ordenado(self, lista1, lista2):
        return sorted(lista1 + lista2)

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        k = k % len(lista)
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_total = n * (n + 1) // 2
        suma_lista = sum(lista)
        return suma_total - suma_lista

    def es_subconjunto(self, conjunto1, conjunto2):
        return set(conjunto1).issubset(set(conjunto2))

    def implementar_pila(self):
        class Pila:
            def __init__(self):
                self.pila = []
            
            def push(self, x):
                self.pila.append(x)
            
            def pop(self):
                return self.pila.pop() if self.pila else None
            
            def peek(self):
                return self.pila[-1] if self.pila else None
            
            def is_empty(self):
                return len(self.pila) == 0
        
        return Pila()
    
    def implementar_cola(self):
        class Cola:
            def __init__(self):
                self.cola = []
            
            def enqueue(self, x):
                self.cola.append(x)
            
            def dequeue(self):
                return self.cola.pop(0) if self.cola else None
            
            def peek(self):
                return self.cola[0] if self.cola else None
            
            def is_empty(self):
                return len(self.cola) == 0
        
        return Cola()

    def matriz_transpuesta(self, matriz):
        return [list(fila) for fila in zip(*matriz)] if matriz else []

