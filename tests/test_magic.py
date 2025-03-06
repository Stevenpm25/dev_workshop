import pytest
from src.magic.magic import Magic

class TestMagic:
    def setup_method(self):
        self.magic = Magic()
    
    def test_fibonacci(self):
        # Test para los primeros números de Fibonacci
        assert self.magic.fibonacci(0) == 0
        assert self.magic.fibonacci(1) == 1
        assert self.magic.fibonacci(2) == 1
        assert self.magic.fibonacci(3) == 2
        assert self.magic.fibonacci(10) == 55
        assert self.magic.fibonacci(10) != 35
    
    def test_secuencia_fibonacci(self):
        # Test para generar secuencia de Fibonacci
        assert self.magic.secuencia_fibonacci(1) == [0]
        assert self.magic.secuencia_fibonacci(2) == [0, 1]
        assert self.magic.secuencia_fibonacci(5) == [0, 1, 1, 2, 3]
        assert self.magic.secuencia_fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    
    def test_es_primo(self):
        # Test para números primos
        assert self.magic.es_primo(2) == True
        assert self.magic.es_primo(7) == True
        assert self.magic.es_primo(17) == True
        # Test para números no primos
        assert self.magic.es_primo(1) == False
        assert self.magic.es_primo(4) == False
        assert self.magic.es_primo(15) == False
        # Test para números negativos
        assert self.magic.es_primo(-5) == False
    
    def test_generar_primos(self):
        # Test para generar números primos hasta n
        assert self.magic.generar_primos(10) == [2, 3, 5, 7]
        assert self.magic.generar_primos(20) == [2, 3, 5, 7, 11, 13, 17, 19]
        # Test para n < 2
        assert self.magic.generar_primos(1) == []
    
    def test_es_numero_perfecto(self):
        # Test para números perfectos
        assert self.magic.es_numero_perfecto(6) == True  # 1 + 2 + 3 = 6
        assert self.magic.es_numero_perfecto(28) == True  # 1 + 2 + 4 + 7 + 14 = 28
        # Test para números no perfectos
        assert self.magic.es_numero_perfecto(10) == False
        assert self.magic.es_numero_perfecto(15) == False
        # Test para 0 y 1
        assert self.magic.es_numero_perfecto(0) == False
        assert self.magic.es_numero_perfecto(1) == False
    
    def test_triangulo_pascal(self):
        # Test para 1 fila
        assert self.magic.triangulo_pascal(1) == [[1]]
        # Test para 3 filas
        assert self.magic.triangulo_pascal(3) == [[1], [1, 1], [1, 2, 1]]
        # Test para 5 filas
        assert self.magic.triangulo_pascal(5) == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    
    def test_factorial(self):
        # Test para factorial
        assert self.magic.factorial(0) == 1
        assert self.magic.factorial(1) == 1
        assert self.magic.factorial(5) == 120
        assert self.magic.factorial(10) == 3628800
    
    def test_mcd(self):
        # Test para máximo común divisor
        assert self.magic.mcd(48, 18) == 6
        assert self.magic.mcd(15, 25) == 5
        assert self.magic.mcd(7, 13) == 1  # Primos entre sí
        assert self.magic.mcd(0, 5) == 5
    
    def test_mcm(self):
        # Test para mínimo común múltiplo
        assert self.magic.mcm(4, 6) == 12
        assert self.magic.mcm(15, 25) == 75
        assert self.magic.mcm(7, 13) == 91
        assert self.magic.mcm(5, 1) == 5
    
    def test_suma_digitos(self):
        # Test para suma de dígitos
        assert self.magic.suma_digitos(123) == 6
        assert self.magic.suma_digitos(9999) == 36
        assert self.magic.suma_digitos(0) == 0
        assert self.magic.suma_digitos(7) == 7
    
    def test_es_numero_armstrong(self):
        # Test para números de Armstrong
        assert self.magic.es_numero_armstrong(153) == True  # 1^3 + 5^3 + 3^3 = 153
        assert self.magic.es_numero_armstrong(370) == True  # 3^3 + 7^3 + 0^3 = 370
        assert self.magic.es_numero_armstrong(371) == True  # 3^3 + 7^3 + 1^3 = 371
        # Test para números que no son de Armstrong
        assert self.magic.es_numero_armstrong(123) == False
        assert self.magic.es_numero_armstrong(100) == False
    
    def test_es_cuadrado_magico(self):
        # Test para cuadrado mágico 3x3
        cuadrado_magico = [
            [2, 7, 6],
            [9, 5, 1],
            [4, 3, 8]
        ]
        assert self.magic.es_cuadrado_magico(cuadrado_magico) == True
        
        # Test para matriz que no es cuadrado mágico
        no_magico = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        assert self.magic.es_cuadrado_magico(no_magico) == False
        
        # Test para cuadrado mágico 1x1
        assert self.magic.es_cuadrado_magico([[5]]) == True