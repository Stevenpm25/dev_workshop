import pytest
import math
from src.geometric.geometric import Geometria

class TestGeometria:
    def setup_method(self):
        self.geometria = Geometria()
    
    def test_area_rectangulo(self):
        # Test con valores enteros positivos
        assert self.geometria.area_rectangulo(5, 4) == 20
        # Test con valores decimales
        assert self.geometria.area_rectangulo(2.5, 3) == 7.5
        # Test con cero (área cero)
        assert self.geometria.area_rectangulo(0, 5) == 0
    
    def test_perimetro_rectangulo(self):
        # Test con valores enteros positivos
        assert self.geometria.perimetro_rectangulo(5, 4) == 18
        # Test con valores decimales
        assert self.geometria.perimetro_rectangulo(2.5, 3) == 11
        # Test con cuadrado (lados iguales)
        assert self.geometria.perimetro_rectangulo(2, 2) == 8
    
    def test_area_circulo(self):
        # Test con radio entero
        assert round(self.geometria.area_circulo(2), 2) == 12.57
        # Test con radio decimal
        assert round(self.geometria.area_circulo(1.5), 2) == 7.07
        # Test con radio cero
        assert self.geometria.area_circulo(0) == 0
    
    def test_perimetro_circulo(self):
        # Test con radio entero
        assert round(self.geometria.perimetro_circulo(2), 2) == 12.57
        # Test con radio decimal
        assert round(self.geometria.perimetro_circulo(1.5), 2) == 9.42
        # Test con radio cero
        assert self.geometria.perimetro_circulo(0) == 0
    
    def test_area_triangulo(self):
        # Test con valores enteros
        assert self.geometria.area_triangulo(6, 4) == 12
        # Test con valores decimales
        assert self.geometria.area_triangulo(5.5, 2.5) == 6.875
        # Test con base cero (área cero)
        assert self.geometria.area_triangulo(0, 5) == 0
    
    def test_perimetro_triangulo(self):
        # Test con triángulo equilátero
        assert self.geometria.perimetro_triangulo(5, 5, 5) == 15
        # Test con triángulo escaleno
        assert self.geometria.perimetro_triangulo(3, 4, 5) == 12
        # Test con valores decimales
        assert self.geometria.perimetro_triangulo(2.5, 3.5, 4.5) == 10.5
    
    def test_es_triangulo_valido(self):
        # Test con triángulo válido
        assert self.geometria.es_triangulo_valido(3, 4, 5) == True
        # Test con triángulo inválido (no cumple la desigualdad triangular)
        assert self.geometria.es_triangulo_valido(1, 2, 10) == False
        # Test con valores negativos (inválido)
        assert self.geometria.es_triangulo_valido(-1, 4, 5) == False
    
    def test_area_trapecio(self):
        # Test con valores enteros
        assert self.geometria.area_trapecio(10, 6, 4) == 32
        # Test con valores decimales
        assert self.geometria.area_trapecio(7.5, 4.5, 3) == 18
        # Test con altura cero (área cero)
        assert self.geometria.area_trapecio(10, 5, 0) == 0
    
    def test_area_rombo(self):
        # Test con valores enteros
        assert self.geometria.area_rombo(8, 6) == 24
        # Test con valores decimales
        assert self.geometria.area_rombo(5.5, 4.5) == 12.375
        # Test con diagonal cero (área cero)
        assert self.geometria.area_rombo(0, 5) == 0
    
    def test_area_pentagono_regular(self):
        # Test con valores enteros
        assert round(self.geometria.area_pentagono_regular(6, 4.1), 2) == 61.5
        # Test con valores decimales
        assert round(self.geometria.area_pentagono_regular(3.5, 2.4), 2) == 21
        # Test con apotema cero (área cero)
        assert self.geometria.area_pentagono_regular(5, 0) == 0
    
    def test_perimetro_pentagono_regular(self):
        # Test con valor entero
        assert self.geometria.perimetro_pentagono_regular(4) == 20
        # Test con valor decimal
        assert self.geometria.perimetro_pentagono_regular(2.5) == 12.5
        # Test con lado cero (perímetro cero)
        assert self.geometria.perimetro_pentagono_regular(0) == 0
    
    def test_area_hexagono_regular(self):
        # Test con valores enteros
        assert round(self.geometria.area_hexagono_regular(5, 4.33), 2) == 64.95
        # Test con valores decimales
        assert round(self.geometria.area_hexagono_regular(2.5, 2.165), 2) == 16.24
        # Test con apotema cero (área cero)
        assert self.geometria.area_hexagono_regular(5, 0) == 0
    
    def test_perimetro_hexagono_regular(self):
        # Test con valor entero
        assert self.geometria.perimetro_hexagono_regular(4) == 24
        # Test con valor decimal
        assert self.geometria.perimetro_hexagono_regular(2.5) == 15
        # Test con lado cero (perímetro cero)
        assert self.geometria.perimetro_hexagono_regular(0) == 0
    
    def test_volumen_cubo(self):
        # Test con valor entero
        assert self.geometria.volumen_cubo(3) == 27
        # Test con valor decimal
        assert self.geometria.volumen_cubo(2.5) == 15.625
        # Test con lado cero (volumen cero)
        assert self.geometria.volumen_cubo(0) == 0
    
    def test_area_superficie_cubo(self):
        # Test con valor entero
        assert self.geometria.area_superficie_cubo(3) == 54
        # Test con valor decimal
        assert self.geometria.area_superficie_cubo(2.5) == 37.5
        # Test con lado cero (área cero)
        assert self.geometria.area_superficie_cubo(0) == 0
    
    def test_volumen_esfera(self):
        # Test con radio entero
        assert round(self.geometria.volumen_esfera(3), 2) == 113.1
        # Test con radio decimal
        assert round(self.geometria.volumen_esfera(2.5), 2) == 65.45
        # Test con radio cero (volumen cero)
        assert self.geometria.volumen_esfera(0) == 0
    
    def test_area_superficie_esfera(self):
        # Test con radio entero
        assert round(self.geometria.area_superficie_esfera(3), 2) == 113.1
        # Test con radio decimal
        assert round(self.geometria.area_superficie_esfera(2.5), 2) == 78.54
        # Test con radio cero (área cero)
        assert self.geometria.area_superficie_esfera(0) == 0
    
    def test_volumen_cilindro(self):
        # Test con valores enteros
        assert round(self.geometria.volumen_cilindro(3, 5), 2) == 141.37
        # Test con valores decimales
        assert round(self.geometria.volumen_cilindro(2.5, 4.2), 2) == 82.47
        # Test con altura cero (volumen cero)
        assert self.geometria.volumen_cilindro(3, 0) == 0
    
    def test_area_superficie_cilindro(self):
        # Test con valores enteros
        assert round(self.geometria.area_superficie_cilindro(3, 5), 2) == 150.8
        # Test con valores decimales
        assert self.geometria.area_superficie_cilindro(2.5, 4.2) == pytest.approx(105.5, rel=1e-2)
        # Test con altura cero (sólo áreas de las bases)
        assert round(self.geometria.area_superficie_cilindro(3, 0), 2) == 56.55
    
    def test_distancia_entre_puntos(self):
        # Test con valores enteros positivos
        assert self.geometria.distancia_entre_puntos(0, 0, 3, 4) == 5
        # Test con valores negativos
        assert self.geometria.distancia_entre_puntos(-1, -2, 2, 3) == 5.83
        # Test con puntos idénticos (distancia cero)
        assert self.geometria.distancia_entre_puntos(5, 5, 5, 5) == 0
    
    def test_punto_medio(self):
        # Test con valores enteros positivos
        assert self.geometria.punto_medio(2, 4, 6, 8) == (4, 6)
        # Test con valores negativos
        assert self.geometria.punto_medio(-2, -4, 2, 4) == (0, 0)
        # Test con valores decimales
        assert self.geometria.punto_medio(1.5, 2.5, 3.5, 4.5) == (2.5, 3.5)
    
    def test_pendiente_recta(self):
        # Test con valores enteros positivos
        assert self.geometria.pendiente_recta(1, 1, 4, 7) == 2
        # Test con valores negativos
        assert self.geometria.pendiente_recta(-1, -2, 2, 4) == 2
        # Test con línea horizontal (pendiente cero)
        assert self.geometria.pendiente_recta(1, 5, 5, 5) == 0
        # Test con línea vertical (pendiente infinita)
        with pytest.raises(ZeroDivisionError):
            self.geometria.pendiente_recta(3, 1, 3, 5)
    
    def test_ecuacion_recta(self):
        # Test con valores enteros
        assert self.geometria.ecuacion_recta(1, 1, 3, 3) == (1.0, -1, 0.0)
        # Test con valores negativos
        assert self.geometria.ecuacion_recta(-1, -2, 2, 4) == (6, -3, 0)
        # Test con línea horizontal
        assert self.geometria.ecuacion_recta(1, 5, 5, 5) == (0, 1, -5)
    
    def test_area_poligono_regular(self):
        # Test con triángulo regular
        assert round(self.geometria.area_poligono_regular(3, 10, 2.89), 2) == 43.35
        # Test con cuadrado
        assert self.geometria.area_poligono_regular(4, 5, 2.5) == 50
        # Test con pentágono
        assert round(self.geometria.area_poligono_regular(5, 6, 4.1), 2) == 61.5
    
    def test_perimetro_poligono_regular(self):
        # Test con triángulo regular
        assert self.geometria.perimetro_poligono_regular(3, 10) == 30
        # Test con cuadrado
        assert self.geometria.perimetro_poligono_regular(4, 5) == 20
        # Test con octágono
        assert self.geometria.perimetro_poligono_regular(8, 2.5) == 20
