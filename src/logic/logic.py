class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        return a and b
    
    def OR(self, a, b):
        return a or b
    
    def NOT(self, a):
        return not a
    
    def XOR(self, a, b):
        return a != b
    
    def NAND(self, a, b):
        return not (a and b)
    
    def NOR(self, a, b):
        return not (a or b)
    
    def XNOR(self, a, b):
        return a == b
    
    def implicacion(self, a, b):
        return not a or b
    
    def bi_implicacion(self, a, b):
        return a == b

    
