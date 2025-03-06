class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def secuencia_fibonacci(self, n):
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq[:n]

    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

    def triangulo_pascal(self, filas):
        resultado = [[1]]
        for i in range(1, filas):
            nueva_fila = [1]
            for j in range(1, i):
                nueva_fila.append(resultado[i - 1][j - 1] + resultado[i - 1][j])
            nueva_fila.append(1)
            resultado.append(nueva_fila)
        return resultado

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        from math import gcd
        return abs(a * b) // gcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        num_str = str(n)
        longitud = len(num_str)
        return sum(int(d) ** longitud for d in num_str) == n

    def es_cuadrado_magico(self, matriz):
        if not matriz or not all(len(fila) == len(matriz) for fila in matriz):
            return False
        suma_ref = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != suma_ref:
                return False
        for col in range(len(matriz)):
            if sum(matriz[fila][col] for fila in range(len(matriz))) != suma_ref:
                return False
        if sum(matriz[i][i] for i in range(len(matriz))) != suma_ref:
            return False
        if sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))) != suma_ref:
            return False
        return True
