class Detector:
    BASES_NITROGENADAS = ["A","C","G","T"]
    CANTIDAD_MAXIMA = 3
    contador = 1
    rango_secuencia = 6

    def __init__(self,adn):
        self.adn = adn


    def detectar_mutantes(self):
        return print(self.mutantes())
    
    def mutantes(self):# Aca gestiono los metodos para detectar mutantes
        if self.horizontal()==True:
            return True
        else:
            return False

    def horizontal(self):
            for i in range(self.rango_secuencia):
                print(f"Primer Contador {self.contador}")
                self.fila = self.adn[i]
                for j in range(1, self.rango_secuencia):
                    if self.fila[j] == self.fila[j-1]:
                        self.contador += 1
                    else:
                        self.contador = 1
                if self.contador > self.CANTIDAD_MAXIMA:
                    print(f"mutante, {self.contador}")
                    return True
                #self.contador = 1
            print(f"no es mutante,Segundo contador {self.contador}")
            return False
    def vertical(self):
            pass
    def diagonal(self):
            pass

class Mutador():
    pass


