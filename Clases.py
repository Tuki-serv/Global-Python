class Detector:
    # Valores que son necesarios para detectar mutantes
    __CANTIDAD_MAXIMA = 3 # Maximo de bases iguales
    __rango_secuencia = 6 # Rango de las secuencias introducidas
    __coordenadas = {# Coordendas para iterar en diagonal
    "d1" : [[3,0],[2,1],[1,2],[0,3]],
    "d2" : [[4,0],[3,1],[2,2],[1,3],[0,4]],
    "d3" : [[5,0],[4,1],[3,2],[2,3],[1,4],[0,5]],
    "d4" : [[5,1],[4,2],[3,3],[2,4],[1,5]],
    "d5" : [[5,2],[4,3],[3,4],[2,5]]
    }

# Método constructor donde se define la referencia de la matriz
# y también un contador de bases
    def __init__(self,adn):
        self.adn = adn
        self.contador = 1

# Metodo principal que llama al metodo gestor
    def detectar_mutantes(self):
        return print(self.mutantes())
    

    def mutantes(self):# Metodo que gestiona las distintas direciones
        if self.vertical() == True or self.horizontal()==True or self.diagonal() == True:
            return True
        else:
            return False
        
    def verficacion(self, lista,rango): #Metodo de verificación
        # Inicializa lo valores a trabajar
        self.identidad = lista
        self.rango = rango
        for j in range(1, self.rango):# Bucle que itera sobre la lista
            # Condición de verificación de lista
            # Se evalua si se repiten bases más de 3 veces
            if self.identidad[j] == self.identidad[j-1]:
                self.contador += 1
            else:
                self.contador = 1
            if self.contador > self.__CANTIDAD_MAXIMA:
                print(self.identidad)
                return True
        return False

    def horizontal(self):# Dirección horizontal
        for i in range(self.__rango_secuencia):# Añade los elementos a una lista y la  verifica
            self.contador = 1
            self.fila = self.adn[i]
            fila = self.fila
            rango = self.__rango_secuencia
            if  self.verficacion(fila,rango) == True:
                print("Horizontal detectada")
                return True
        return False

    def vertical(self):# Dirección vertical
        for i in range(self.__rango_secuencia):# Añade los elementos a una lista y la  verifica
            self.contador = 1
            self.columna = [self.adn[j][i] for j in range(self.__rango_secuencia)]
            fila = self.columna
            rango = (self.__rango_secuencia)
            if self.verficacion(fila,rango):
                print("Vertical detectada")
                return True
        return False

    def diagonal(self):# Dirección diagonal
        self.orden = 2 # Valor de control
        self.contador = 1
        for i in range(self.orden):# Segun el valor de control devuelve un lista
            if i == 1:# La lista puede ser la original o la inversa
                self.matriz = [list(reversed(sublista)) for sublista in self.adn]
            else:
                self.matriz = self.adn
            for d in self.__coordenadas.values():# Añade los elementos a una lista y la  verifica
                self.elementos = [self.matriz[j[0]][j[1]] for j in d]
                fila = self.elementos
                rango = len(self.elementos)
                if self.verficacion(fila,rango) == True:
                    print("Diagonal detectada")
                    return True
        return False

class Mutador():# Superclase Mutador
    def __init__(self,base):
        self.base_nitrogenda = base
    def crear_mutante(self,):
        pass

class Radiacion(Mutador):
    def __init__(self,base):
        super().__init__(base)
    
    pass

class Viruz(Mutador):
    pass