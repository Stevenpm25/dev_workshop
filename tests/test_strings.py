import pytest

from src.string.strings import Strings


class TestStrings:
    def setup_method(self):
        self.strings = Strings()
    
    def test_es_palindromo(self):
        assert self.strings.es_palindromo("ana") == True
        assert self.strings.es_palindromo("reconocer") == True
        assert self.strings.es_palindromo("Anita lava la tina") == True
        assert self.strings.es_palindromo("sigmotoa") == False
        assert self.strings.es_palindromo("mundo") == False
        assert self.strings.es_palindromo("") == True
    
    def test_invertir_cadena(self):
        assert self.strings.invertir_cadena("hola") == "aloh"
        assert self.strings.invertir_cadena("Python") == "nohtyP"
        assert self.strings.invertir_cadena("sigmotoA") == "Aotomgis"
        assert self.strings.invertir_cadena("") == ""
        assert self.strings.invertir_cadena("a") == "a"
    
    def test_contar_vocales(self):
        assert self.strings.contar_vocales("sigmotoa") == 4
        assert self.strings.contar_vocales("murcielago") == 5
        assert self.strings.contar_vocales("rhythm") == 0
        assert self.strings.contar_vocales("AeIoU") == 5
        assert self.strings.contar_vocales("") == 0
    
    def test_contar_consonantes(self):
        assert self.strings.contar_consonantes("sigmotoa") == 4
        assert self.strings.contar_consonantes("Python") == 4
        assert self.strings.contar_consonantes("aeiou") == 0
        assert self.strings.contar_consonantes("PythOn") == 4
        assert self.strings.contar_consonantes("") == 0
    
    def test_es_anagrama(self):
        assert self.strings.es_anagrama("roma", "amor") == True
        assert self.strings.es_anagrama("listen", "silent") == True
        assert self.strings.es_anagrama("ekans","sneak") == True
        assert self.strings.es_anagrama("Dormitory", "Dirty room") == True
        assert self.strings.es_anagrama("hello", "world") == False
        assert self.strings.es_anagrama("python", "typhons") == False
    
    def test_contar_palabras(self):
        assert self.strings.contar_palabras("Hola mundo") == 2
        assert self.strings.contar_palabras("Python es divertido") == 3
        assert self.strings.contar_palabras("  dev with sigmotoa    ") == 3
        assert self.strings.contar_palabras("") == 0
    
    def test_palabras_mayus(self):
        assert self.strings.palabras_mayus("hola mundo") == "Hola Mundo"
        assert self.strings.palabras_mayus("sigmotoa es genial") == "Sigmotoa Es Genial"
        assert self.strings.palabras_mayus("Hola Mundo") == "Hola Mundo"
        assert self.strings.palabras_mayus("  hola  mundo  ") == "  Hola  Mundo  "
        assert self.strings.palabras_mayus("") == ""
    
    def test_eliminar_espacios_duplicados(self):
        assert self.strings.eliminar_espacios_duplicados("Hola  mundo") == "Hola mundo"
        assert self.strings.eliminar_espacios_duplicados("  sigmotoa   es   genial  ") == " sigmotoa es genial "
        assert self.strings.eliminar_espacios_duplicados("Hola mundo") == "Hola mundo"
        assert self.strings.eliminar_espacios_duplicados("") == ""
    
    def test_es_numero_entero(self):
        assert self.strings.es_numero_entero("123") == True
        assert self.strings.es_numero_entero("-456") == True
        assert self.strings.es_numero_entero("12.34") == False
        assert self.strings.es_numero_entero("abc") == False


