import pytest

from src.string.strings import Strings


class TestStrings:
    def setup_method(self):
        self.strings = Strings()
    
    def test_es_palindromo(self):
        # Test con palíndromos simples
        assert self.strings.es_palindromo("ana") == True
        assert self.strings.es_palindromo("reconocer") == True
        # Test con palíndromos con espacios y mayúsculas
        assert self.strings.es_palindromo("Anita lava la tina") == True
        # Test con no palíndromos
        assert self.strings.es_palindromo("sigmotoa") == False
        assert self.strings.es_palindromo("mundo") == False
        # Test con cadena vacía
        assert self.strings.es_palindromo("") == True
    
    def test_invertir_cadena(self):
        # Test con cadenas simples
        assert self.strings.invertir_cadena("hola") == "aloh"
        assert self.strings.invertir_cadena("Python") == "nohtyP"
        assert self.strings.invertir_cadena("sigmotoA") == "Aotomgis"
        # Test con cadena vacía
        assert self.strings.invertir_cadena("") == ""
        # Test con un solo carácter
        assert self.strings.invertir_cadena("a") == "a"
    
    def test_contar_vocales(self):
        # Test con cadenas con vocales
        assert self.strings.contar_vocales("sigmotoa") == 4
        assert self.strings.contar_vocales("murcielago") == 5
        # Test con cadena sin vocales
        assert self.strings.contar_vocales("rhythm") == 0
        # Test con vocales en mayúsculas y minúsculas
        assert self.strings.contar_vocales("AeIoU") == 5
        # Test con cadena vacía
        assert self.strings.contar_vocales("") == 0
    
    def test_contar_consonantes(self):
        # Test con cadenas con consonantes
        assert self.strings.contar_consonantes("sigmotoa") == 4
        assert self.strings.contar_consonantes("Python") == 4
        # Test con cadena sin consonantes
        assert self.strings.contar_consonantes("aeiou") == 0
        # Test con consonantes en mayúsculas y minúsculas
        assert self.strings.contar_consonantes("PythOn") == 4
        # Test con cadena vacía
        assert self.strings.contar_consonantes("") == 0
    
    def test_es_anagrama(self):
        # Test con anagramas simples
        assert self.strings.es_anagrama("roma", "amor") == True
        assert self.strings.es_anagrama("listen", "silent") == True
        assert self.strings.es_anagrama("ekans","sneak") == True
        # Test con anagramas con mayúsculas
        assert self.strings.es_anagrama("Dormitory", "Dirty room") == True
        # Test con no anagramas
        assert self.strings.es_anagrama("hello", "world") == False
        # Test con cadenas de diferente longitud
        assert self.strings.es_anagrama("python", "typhons") == False
    
    def test_contar_palabras(self):
        # Test con frases simples
        assert self.strings.contar_palabras("Hola mundo") == 2
        assert self.strings.contar_palabras("Python es divertido") == 3
        # Test con espacios múltiples
        assert self.strings.contar_palabras("  dev with sigmotoa    ") == 3
        # Test con cadena vacía
        assert self.strings.contar_palabras("") == 0
    
    def test_palabras_mayus(self):
        # Test con frases simples
        assert self.strings.palabras_mayus("hola mundo") == "Hola Mundo"
        assert self.strings.palabras_mayus("sigmotoa es genial") == "Sigmotoa Es Genial"
        # Test con palabras ya capitalizadas
        assert self.strings.palabras_mayus("Hola Mundo") == "Hola Mundo"
        # Test con espacios múltiples
        assert self.strings.palabras_mayus("  hola  mundo  ") == "  Hola  Mundo  "
        # Test con cadena vacía
        assert self.strings.palabras_mayus("") == ""
    
    def test_eliminar_espacios_duplicados(self):
        # Test con espacios múltiples
        assert self.strings.eliminar_espacios_duplicados("Hola  mundo") == "Hola mundo"
        assert self.strings.eliminar_espacios_duplicados("  sigmotoa   es   genial  ") == " sigmotoa es genial "
        # Test sin espacios duplicados
        assert self.strings.eliminar_espacios_duplicados("Hola mundo") == "Hola mundo"
        # Test con cadena vacía
        assert self.strings.eliminar_espacios_duplicados("") == ""
    
    def test_es_numero_entero(self):
        # Test con números enteros
        assert self.strings.es_numero_entero("123") == True
        assert self.strings.es_numero_entero("-456") == True
        # Test con números no enteros
        assert self.strings.es_numero_entero("12.34") == False

