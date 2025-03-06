import re
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
        texto = ''.join(filter(str.isalnum, texto.lower()))  # Elimina espacios y caracteres no alfanuméricos
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
        return sum(1 for char in texto.lower() if char in "aeiou")

    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ" 
        return sum(1 for c in texto if c in consonantes)


    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        """
        texto1 = ''.join(sorted(texto1.lower().replace(" ", "")))
        texto2 = ''.join(sorted(texto2.lower().replace(" ", "")))
        return texto1 == texto2

    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        """
        return len(texto.split())

    def palabras_mayus(self, texto):
        """
        Pone en mayúscula la primera letra de cada palabra en una cadena.
        """
        return texto.title()

    def eliminar_espacios_duplicados(self, texto):
        texto_sin_duplicados = re.sub(r'\s+', ' ', texto)  
        if texto.startswith(" "):  
            texto_sin_duplicados = " " + texto_sin_duplicados.lstrip()
        if texto.endswith(" "):  
            texto_sin_duplicados = texto_sin_duplicados.rstrip() + " "
        return texto_sin_duplicados

    def es_numero_entero(self, cadena):
        """
        Verifica si una cadena representa un número entero (positivo o negativo).
        """
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
                resultado += char  # Mantiene espacios y otros caracteres sin cambios
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




