class Detector:
    BASES_NITROGENADAS = ["A","C","G","T"]
    CANTIDAD_MAXIMA = 3
    rango_secuencia = 6

    def __init__(self,adn):
        self.adn = adn
        self.contador = 1


    def detectar_mutantes(self):
        return print(self.mutantes())
    
    def mutantes(self):# Aca gestiono los metodos para detectar mutantes
        #if self.horizontal()==True:
        if self.vertical() == True:
            return True
        else:
            print("Chau")
            return False

    def horizontal(self):
        for i in range(self.rango_secuencia):
            self.contador = 1
            self.fila = self.adn[i]
            for j in range(1, self.rango_secuencia):
                if self.fila[j] == self.fila[j-1]:
                    self.contador += 1
                else:
                    self.contador = 1
                if self.contador > self.CANTIDAD_MAXIMA:
                    return True
            return False

    def vertical(self):
        for i in range(self.rango_secuencia):
            self.columna = [self.adn[j][i] for j in range(self.rango_secuencia)]
            print(f"{self.columna}")
            for a in range(1, self.rango_secuencia):
                if self.columna[a] == self.columna[a-1]:
                    self.contador += 1
                else:
                    self.contador = 1
                if self.contador > self.CANTIDAD_MAXIMA:
                    return True
            print("hola")
            return False

    def diagonal(self):
            pass

class Mutador():
    pass


