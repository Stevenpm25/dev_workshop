import pytest
from src.data.data import Data

class TestData:
    def setup_method(self):
        self.data = Data()
    
    def test_invertir_lista(self):
        # Test con lista de enteros
        assert self.data.invertir_lista([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
        # Test con lista vacía
        assert self.data.invertir_lista([]) == []
        # Test con lista de un elemento
        assert self.data.invertir_lista([42]) == [42]
        # Test con lista de strings
        assert self.data.invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
    
    def test_buscar_elemento(self):
        # Test con elemento presente
        assert self.data.buscar_elemento([10, 20, 30, 40, 50], 30) == 2
        # Test con elemento no presente
        assert self.data.buscar_elemento([10, 20, 30, 40, 50], 60) == -1
        # Test con elemento repetido (debe retornar el primer índice)
        assert self.data.buscar_elemento([10, 20, 30, 20, 50], 20) == 1
        # Test con lista vacía
        assert self.data.buscar_elemento([], 42) == -1
    
    def test_eliminar_duplicados(self):
        # Test con lista con duplicados
        assert self.data.eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
        # Test con lista sin duplicados
        assert self.data.eliminar_duplicados([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        # Test con lista vacía
        assert self.data.eliminar_duplicados([]) == []
        # Test con valores de diferentes tipos
        assert self.data.eliminar_duplicados([1, "a", 1, "a", True]) == [1, "a", True]
    
    def test_merge_ordenado(self):
        # Test con listas de enteros ordenadas
        assert self.data.merge_ordenado([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        # Test con una lista vacía
        assert self.data.merge_ordenado([], [1, 2, 3]) == [1, 2, 3]
        # Test con ambas listas vacías
        assert self.data.merge_ordenado([], []) == []
        # Test con listas con elementos repetidos
        assert self.data.merge_ordenado([1, 2, 3], [1, 3, 5]) == [1, 1, 2, 3, 3, 5]
    
    def test_rotar_lista(self):
        # Test con rotación positiva
        assert self.data.rotar_lista([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
        # Test con rotación mayor que longitud de la lista
        assert self.data.rotar_lista([1, 2, 3], 5) == [2, 3, 1]
        # Test con rotación cero
        assert self.data.rotar_lista([1, 2, 3], 0) == [1, 2, 3]
        # Test con lista vacía
        assert self.data.rotar_lista([], 3) == []
    
    def test_encuentra_numero_faltante(self):
        # Test con número faltante en el medio
        assert self.data.encuentra_numero_faltante([1, 2, 4, 5]) == 3
        # Test con número faltante al principio
        assert self.data.encuentra_numero_faltante([2, 3, 4, 5]) == 1
        # Test con número faltante al final
        assert self.data.encuentra_numero_faltante([1, 2, 3, 4]) == 5
    
    def test_es_subconjunto(self):
        # Test con subconjunto verdadero
        assert self.data.es_subconjunto([1, 2], [1, 2, 3, 4]) == True
        # Test con no subconjunto
        assert self.data.es_subconjunto([1, 5], [1, 2, 3, 4]) == False
        # Test con conjuntos iguales
        assert self.data.es_subconjunto([1, 2, 3], [1, 2, 3]) == True
        # Test con conjunto vacío
        assert self.data.es_subconjunto([], [1, 2, 3]) == True
    
    def test_implementar_pila(self):
        pila = self.data.implementar_pila()
        # Test de pila vacía
        assert pila["is_empty"]() == True
        # Test de push y peek
        pila["push"](1)
        assert pila["peek"]() == 1
        pila["push"](2)
        assert pila["peek"]() == 2
        # Test de pop
        assert pila["pop"]() == 2
        assert pila["pop"]() == 1
        assert pila["is_empty"]() == True
    
    def test_implementar_cola(self):
        cola = self.data.implementar_cola()
        # Test de cola vacía
        assert cola["is_empty"]() == True
        # Test de enqueue y peek
        cola["enqueue"](1)
        assert cola["peek"]() == 1
        cola["enqueue"](2)
        assert cola["peek"]() == 1
        # Test de dequeue
        assert cola["dequeue"]() == 1
        assert cola["dequeue"]() == 2
        assert cola["is_empty"]() == True
    
    def test_matriz_transpuesta(self):
        # Test con matriz 2x3
        matriz = [[1, 2, 3], [4, 5, 6]]
        resultado = [[1, 4], [2, 5], [3, 6]]
        assert self.data.matriz_transpuesta(matriz) == resultado
        # Test con matriz cuadrada
        matriz = [[1, 2], [3, 4]]
        resultado = [[1, 3], [2, 4]]
        assert self.data.matriz_transpuesta(matriz) == resultado
        # Test con matriz 1x1
        assert self.data.matriz_transpuesta([[5]]) == [[5]]
        # Test con matriz vacía
        assert self.data.matriz_transpuesta([]) == []