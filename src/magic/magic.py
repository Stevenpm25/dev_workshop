import math
from functools import lru_cache

class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """

    @lru_cache(None)
    def fibonacci(self, n):
        """Calcula el n-ésimo número de Fibonacci usando memoización para optimización."""
        if n < 0:
            raise ValueError("El índice de Fibonacci no puede ser negativo")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def secuencia_fibonacci(self, n):
        """Genera una secuencia de Fibonacci de longitud n."""
        if n <= 0:
            return []
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq[:n]

    def es_primo(self, n):
        """Determina si un número es primo."""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        """Genera una lista de números primos hasta n (incluido)."""
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        """Determina si un número es perfecto (igual a la suma de sus divisores propios)."""
        if n <= 0:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n

    def triangulo_pascal(self, filas):
        """Genera el triángulo de Pascal con el número de filas especificado."""
        if filas <= 0:
            return []
        resultado = [[1]]
        for i in range(1, filas):
            nueva_fila = [1] + [resultado[i - 1][j - 1] + resultado[i - 1][j] for j in range(1, i)] + [1]
            resultado.append(nueva_fila)
        return resultado

    def factorial(self, n):
        """Calcula el factorial de un número usando math.factorial."""
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        return math.factorial(n)

    def mcd(self, a, b):
        """Calcula el máximo común divisor (MCD) usando el algoritmo de Euclides."""
        return math.gcd(a, b)

    def mcm(self, a, b):
        """Calcula el mínimo común múltiplo (MCM) de dos números."""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // math.gcd(a, b)

    def suma_digitos(self, n):
        """Suma los dígitos de un número entero."""
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        """Determina si un número es un número de Armstrong (narcisista)."""
        num_str = str(n)
        longitud = len(num_str)
        return sum(int(d) ** longitud for d in num_str) == n

    def es_cuadrado_magico(self, matriz):
        """Determina si una matriz cuadrada es un cuadrado mágico."""
        if not matriz or any(len(fila) != len(matriz) for fila in matriz):
            return False

        suma_ref = sum(matriz[0])  # Suma de referencia (primera fila)
        
        # Verificar filas y columnas
        for i in range(len(matriz)):
            if sum(matriz[i]) != suma_ref or sum(matriz[j][i] for j in range(len(matriz))) != suma_ref:
                return False
        
        # Verificar diagonales
        if sum(matriz[i][i] for i in range(len(matriz))) != suma_ref:
            return False
        if sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))) != suma_ref:
            return False

        return True

