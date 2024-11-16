import random
class Detector:
    # Valores que son necesarios para detectar mutantes
    __CANTIDAD_MAXIMA = 3 # Maximo de bases iguales
    rango_secuencia = 6 # Rango de las secuencias introducidas
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
    def detectar_mutantes(self,):
        return self.mutantes()
    

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
                return True
        return False

    """
    Los metodos de dirección en esta clase generan una lista de la secuencia correspondiente
    esta lista es pasada al método de verificación donde se evalua si contine mutantes
    """

    def horizontal(self):# Dirección horizontal
        for i in range(self.rango_secuencia):# Añade los elementos a una lista y la  verifica
            self.contador = 1
            self.fila = self.adn[i]
            fila = self.fila
            rango = self.rango_secuencia
            if  self.verficacion(fila,rango) == True:
                return True
        return False

    def vertical(self):# Dirección vertical
        for i in range(self.rango_secuencia):# Añade los elementos a una lista y la  verifica
            self.contador = 1
            self.columna = [self.adn[j][i] for j in range(self.rango_secuencia)]
            fila = self.columna
            rango = (self.rango_secuencia)
            if self.verficacion(fila,rango):
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
                    return True
        return False

class Sanador(Detector):
    __BASES_NITROGENADAS = ["A","C","G","T"]
    def __init__(self,adn):
        super().__init__(adn)

    def sanar_mutantes(self):# En este metodo se genera una secuencia nueva si el método heredado retorna verdadero
        if self.detectar_mutantes() == True:
            print("La secuencia de ADN contiene mutaciones, comienza la curación\n""")
            while True:
                self.adn = [[random.choice(self.__BASES_NITROGENADAS) for i in range(self.rango_secuencia)] for i in range(self.rango_secuencia)]
                if self.detectar_mutantes() == False:
                    print("Secuencia curada con exito")
                    return self.adn
        else:
            print("La secuencia de ADN no contiene mutaciones")

class Mutador():# Superclase Mutador
    rango_secuencia = 6
    cantidad = 4

    def __init__(self,adn,base,direccion):
        self.adn = adn
        self.base = base
        self.direccion = direccion

    def crear_mutante(self,):# Método abtracto
        print("Elija la cordenada donde quiere genrar el mutante\n")
        self.mostras_coordenadas()
        print("----------------------------------")

    def mostras_coordenadas(self):# Método que imprime una matriz para que el usuario elija el lugar
        normal = [[f"F:{i} C:{j}| " for j in range(6)] for i in range(6)]
        print("F: Fila | C: Columna")
        return print("\n".join("  ".join(normal[i][j] for j in range(6)) for i in range(6)))
        

class Radiacion(Mutador):
    def __init__(self,adn,base,direccion):
        super().__init__(adn,base,direccion)

    def crear_mutante(self):
        if self.direccion == 1:
            while True:
                try:
                    super().crear_mutante()
                    origen = list(input("Ingrese la coordenada (fila, columna): "))
                    origen = list(map(int, origen))

                    for i in range(origen[1], origen[1] + self.cantidad):
                        self.adn[origen[0]][i] = self.base
                        
                    print("Mutante creado")
                    return self.adn
                
                except ValueError :
                    print(f"Error. Ingrese solo números")
                except IndexError:
                    print("Error: Fuera de rango de la matriz, la base se repite 4 veces dentro de un rango 0 a 5")
        else:
            while True:
                try:
                    super().crear_mutante()
                    origen = list(input("Ingrese la coordenada (fila, columna): "))
                    origen = list(map(int, origen))

                    for i in range(origen[0], origen[0] + self.cantidad):
                        self.adn[i][origen[1]] = self.base

                    print("Mutante creado")
                    return self.adn
                
                except ValueError :
                    print(f"Error. Ingrese solo números")
                except IndexError:
                    print("Error: Fuera de rango de la matriz, la base se repite 4 veces dentro de un rango 0 a 5")

class Viruz(Mutador):
    __coordenadas = {# Coordendas para iterar en diagonal
    "d1" : [[3,0],[2,1],[1,2],[0,3]],
    "d2" : [[4,0],[3,1],[2,2],[1,3],[0,4]],
    "d3" : [[5,0],[4,1],[3,2],[2,3],[1,4],[0,5]],
    "d4" : [[5,1],[4,2],[3,3],[2,4],[1,5]],
    "d5" : [[5,2],[4,3],[3,4],[2,5]]
    }

    def __init__(self,adn,base,direccion):
        super().__init__(adn,base,direccion)

    def sentido(self):
        print("En que sentido queres generar el mutante?")
        while True:
            self.direccion=int(input("Ascendente: 1 | Descendente: 2 | : "))
            if self.direccion in (1,2):
                break

    def crear_mutante(self):
        if self.direccion == 1:
            while True:
                try:
                    origen = list(input("Ingrese la coordenada (fila, columna): "))
                    origen = list(map(int, origen))

                    for d in self.__coordenadas.values():# Añade los elementos a una lista y la  verifica
                        self.elementos = [self.adn[j[0]][j[1]] for j in d]
                    
                    
                    pass 
                except:
                    pass
        pass

    
"""
adn = [
    ['A', 'C', 'G', 'T', 'A', 'C'],
    ['G', 'T', 'A', 'C', 'G', 'T'],
    ['A', 'C', 'G', 'T', 'A', 'C'],
    ['G', 'T', 'A', 'C', 'G', 'T'],
    ['A', 'C', 'G', 'T', 'A', 'C'],
    ['G', 'T', 'A', 'C', 'G', 'T']
]
"""