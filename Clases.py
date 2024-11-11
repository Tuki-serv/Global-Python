class Detector:
    CANTIDAD_MAXIMA = 3
    rango_secuencia = 6
    coordenadas = {
    "d1" : [[3,0],[2,1],[1,2],[0,3]],
    "d2" : [[4,0],[3,1],[2,2],[1,3],[0,4]],
    "d3" : [[5,0],[4,1],[3,2],[2,3],[1,4],[0,5]],
    "d4" : [[5,1],[4,2],[3,3],[2,4],[1,5]],
    "d5" : [[5,2],[4,3],[3,4],[2,5]]
    }


    def __init__(self,adn):
        self.adn = adn
        self.contador = 1


    def detectar_mutantes(self):
        return print(self.mutantes())
    
    def mutantes(self):# Aca gestiono los metodos para detectar mutantes
        if self.vertical() == True or self.horizontal()==True or self.diagonal() == True:
        #if self.diagonal() == True:
            return True
        else:
            print("Chau")
            return False
    def verficacion(self, lista,rango):
        self.identidad = lista
        self.rango = rango
        for j in range(1, self.rango):
            if self.identidad[j] == self.identidad[j-1]:
                self.contador += 1
            else:
                self.contador = 1
            if self.contador > self.CANTIDAD_MAXIMA:
                print(self.identidad)
                return True
        return False

    def horizontal(self):
        for i in range(self.rango_secuencia):
            self.contador = 1
            self.fila = self.adn[i]
            fila = self.fila
            rango = self.rango_secuencia
            if  self.verficacion(fila,rango) == True:
                print("Horizontal detectada")
                return True
        return False

    def vertical(self):
        for i in range(self.rango_secuencia):
            self.contador = 1
            self.columna = [self.adn[j][i] for j in range(self.rango_secuencia)]
            fila = self.columna
            rango = (self.rango_secuencia)
            if self.verficacion(fila,rango):
                print("Vertical detectada")
                return True
        return False

    def diagonal(self):
        self.orden = 2
        self.contador = 1
        for i in range(self.orden):
            if i == 1:
                self.matriz = [list(reversed(sublista)) for sublista in self.adn]
            else:
                self.matriz = self.adn
            for d in self.coordenadas.values():
                self.elementos = [self.matriz[j[0]][j[1]] for j in d]
                fila = self.elementos
                rango = len(self.elementos)
                if self.verficacion(fila,rango) == True:
                    print("Diagonal detectada")
                    return True
        return False

class Mutador():
    pass

