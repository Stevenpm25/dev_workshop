class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        Ignora espacios y mayúsculas.
        """
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]

    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        """
        resultado = ""
        for char in texto:
            resultado = char + resultado  # Agrega cada letra al inicio
        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        """
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char in vocales)
    
    def contar_consonantes(self, cadena):
        consonantes = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        return sum(1 for c in cadena if c in consonantes)
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        """
        texto1 = texto1.lower().replace(" ", "")
        texto2 = texto2.lower().replace(" ", "")
        return sorted(texto1) == sorted(texto2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        """
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pone en mayúscula la primera letra de cada palabra en una cadena.
        """
        return ' '.join(palabra.capitalize() for palabra in texto.split(' '))

    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())
    

    def es_numero_entero(self, cadena):
        return cadena.lstrip("-+").isdigit()

    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        """
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                resultado += char  # Mantiene espacios y otros caracteres iguales
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        """
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        """
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones





