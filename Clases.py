import random
import os

class Detector:
    """
    Esta es la clase detector que verifica por cada dirección
    de la matriz si existen mutantes
    """
    # Valores que son necesarios para detectar mutantes
    CANTIDAD_MAXIMA = 3 # Maximo de bases iguales
    rango_secuencia = 6 # Rango de las secuencias introducidas
    coordenadas = {# Coordendas para iterar en diagonal
    "d1" : [(3, 0), (2, 1), (1, 2), (0, 3)],
    "d2" : [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
    "d3" : [(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)],
    "d4" : [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)],
    "d5" : [(5, 2), (4, 3), (3, 4), (2, 5)]
    }

# Método constructor donde se define la referencia de la matriz
# y también un contador de bases
    def __init__(self,adn: list) -> None:
        self.adn = adn
        self.contador = 1

# Metodo principal que llama al metodo gestor
    def detectar_mutantes(self) -> bool:
        return self.mutantes()
    

    def mutantes(self) -> bool:# Metodo que gestiona las distintas direciones
        """
        Retorno True = Existen mutaciones en alguna dirección
        Retorno False = No existen mutaciones en ninguna dirección
        """
        if  self.direcciones("horizontal") or self.direcciones("vertical") or self.direcciones("diagonal") or self.direcciones("diagonal.invertida"):
            return True
        else:
            return False
        
    def verficacion(self, lista: list, rango: int) -> bool: #Metodo de verificación
        # Inicializa lo valores a trabajar
        self.identidad = lista
        self.rango = rango
        """
        Si contador no supera la cantidad maxima retorna false
        """
        for j in range(1, self.rango):# Bucle que itera sobre la lista
            """ Condición de verificación de lista
            Se evalua si se repiten bases más de 3 veces"""
            if self.identidad[j] == self.identidad[j-1]:# Verifica si un elemento es igual a su anterior
                self.contador += 1 # Si es igual, contador aumenta en 1 
            else:
                self.contador = 1 # Si no es igual, contador vuelve a 1

            if self.contador > self.CANTIDAD_MAXIMA: # Verifica si contador es mayor a la cantidad maxima aceptable
                return True
        return False

    def direcciones(self, direccion: str) -> bool:
        """
        Crea una lista segun la dirección y la verifica
        """
        if direccion == "horizontal":
            secuencias = [self.adn[fila] for fila in range(self.rango_secuencia)]
        elif direccion == "vertical":
            secuencias = [[self.adn[fila][columna] for fila in range(self.rango_secuencia)] for columna in range(self.rango_secuencia)]
        elif direccion == "diagonal":
            secuencias = self.diagonales(1)
        elif direccion == "diagonal.invertida":
            secuencias = self.diagonales(2)
        for secuecia in secuencias:# Verifica
            if self.verficacion(secuecia,len(secuecia)):
                return True
        return False

    def diagonales(self,control: int) -> list:
        """
        Genera todas las diagonales de la matriz segun las coordenadas (ascendentes y descendentes).
        """
        diagonales = []
        if control == 1:
            for i in self.coordenadas.values():
                diagonales.append([self.adn[x][y] for x, y in i])
        else: 
            matriz = self.adn
            matriz = [list(reversed(sublista)) for sublista in self.adn]
            for j in self.coordenadas.values():
                diagonales.append([matriz[x][y] for x, y in j])
        return diagonales
class Sanador(Detector):
    """
    Esta la Clase sanador, hereda métodos de la Clase Detector

    """
    __BASES_NITROGENADAS = ["A","C","G","T"] # Lista de las bases que contiene la matriz
    def __init__(self,adn: list) -> None:
        super().__init__(adn) # Inicializa el método constructor de la superclase

    def sanar_mutantes(self) -> list:
        """
        En este metodo se genera una matriz nueva
        si el método heredado (detectar_mutantes) retorna verdadero
        Caso contrario retorna la matriz introducida
        """
        if self.detectar_mutantes() == True:
            print("\nLa secuencia de ADN contiene mutaciones, comienza la curación")
            while True:
                """
                Mientras la nueva matriz contenga mutaciones, se generara otra matriz
                """
                # Se genera una nueva matriz con las bases selecionadas aleatoriamente
                self.adn = [[random.choice(self.__BASES_NITROGENADAS) for i in range(self.rango_secuencia)] for i in range(self.rango_secuencia)]
                if self.detectar_mutantes() == False: # Se verifica que la nueva matriz no contenga mutantes 
                    print("\nSecuencia curada con exito")
                    return self.adn
        else:
            print("\nLa secuencia de ADN no contiene mutaciones")
            return self.adn

class Mutador():
    """
    Esta es la superclase mutador, contiene métodos que van
    a ser utilizados por las clases hijas

    Se considera mutar a que una matriz(AND)
    contenga un secuencia de más de 3 bases
    iguales
    """ # Cantidad de veces que se repite la base

    def __init__(self) -> None:# Metodo constructor
        self.cantidad = 4
        self.coordenadas = {# Coordendas para iterar en diagonal
    "1" : [[3, 0], [2, 1], [1, 2], [0, 3]],
    "2" : [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]],
    "3" : [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]],
    "4" : [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],
    "5" : [[5, 2], [4, 3], [3, 4], [2, 5]]
    }
        #self.adn = adn
        #self.base = base
        #self.direccion = direccion

    def crear_mutante(self) -> None:# Método polimorfico que crea mutaciones
        """
        Método polimorfico que crea mutaciones
        tambíen llama a otros metodos necesarios para mejorar la visualización
        """
        pass
        """self.separar()
        print("\nElija donde quiere generar el mutante")
        self.mostrar_coordenadas()
        self.separar()"""

    def mostrar_coordenadas(self) -> None:
        """
        Método que imprime una matriz con el fin de que el usuario
        pueda ver las coordenadas de todas las posiciones 
        """
        normal = [[f"F:{i} C:{j}| " for j in range(6)] for i in range(6)] # Se crea una matriz
        print("\nF: Fila | C: Columna") # Muestra al usuario como guiarse por la matriz
        self.separar()
        print("\n".join("  ".join(normal[i][j] for j in range(6)) for i in range(6)))# Imprime la matriz
    
    def separar(self) -> None:
        """
        Este método crea una línea para separar
        se creo para mas facilidad en el uso
        """
        print("---------------------------------------------------------------")
    
    def limpiar_consola(self) -> None:
        """
        Método que limpia la consola de ser necesario
        Su uso es cuando ya no es necesaria mostrar cierta información
        """
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para sistemas Unix (Linux/macOS)
            os.system('clear')


class Radiacion(Mutador):
    """
    Subclase encargada de mutar el ADN
    Solo muta en Horizontal y Vertical
    """
    def __init__(self) -> None:# Inicializa el método contructor de la superclase
        super().__init__()

    def crear_mutante(self,adn: list,base: str,direccion: int) -> list:
        self.adn = adn
        self.base = base
        self.direccion = direccion
        """
        Método heredado modificado
        Mientras se respete el fomato este método retorna una matriz modificada
        en caso contrario se le pedira al usuario que lo intente de nuevo
        """
        while True:
            try:
                print("\nElija donde quiere generar el mutante")
                print("\nMutante Horizontal") if self.direccion == 1 else print("\nMutante Vertical") # Muestra la dirección del usuario
                self.mostrar_coordenadas()
                # Pedir las coordenadas desde donde se inicia la mutación
                origen = input("\nIngrese la coordenada (Fila, Columna| Formato Ejemplo: 21): ")
                if len(origen) != 2:# Se crea una instancia de error si se la entrada es diferente al formato
                    raise ValueError("Ingrese solamente dos números seguidos: xy")
                fila, columna = map(int, origen)# Descompongo la lista en dos variables
                
                # Determinar los desplazamientos según la dirección
                if self.direccion == 1:  # Horizontal
                    indices = [(fila, columna + i) for i in range(self.cantidad)]
                else:  # Vertical
                    indices = [(fila + i, columna) for i in range(self.cantidad)]
                
                # Cambia los valores de las coordenadas de la matriz por la base ingresada por el usuario
                for x, y in indices:
                    self.adn[x][y] = self.base
                
                # Se retorna la matriz modificada
                print("\nMutante creado")
                return self.adn
            
            # Razones para pedir al usuario que lo intente devuelta
            except ValueError as error:# Ingresar mal los datos
                self.limpiar_consola()
                self.separar()
                print(f"\nError. {error}")
            except IndexError:# Ingresar un origen que produzca iterar fuera de la matriz
                self.limpiar_consola()
                self.separar()
                print("\nError: Fuera de rango de la matriz, la base se repite 4 veces dentro de un rango 0 a 5")

class Viruz(Mutador):
    """
    Subclase encargada de mutar el ADN en diagonal
    Muta en sentido Ascendente y Descendente
    """

    def __init__(self) -> None: # Inicializa el método constructor de la superclase
        super().__init__()

    def mostrar_coordenadas(self) -> None:
        """
        Se cambio la lógica para adaptarse a la subclase 
        Sigue teniendo el mismo fin (ayudar al usuario a ver graficamente la matriz)
        Pero esta vez muestra las filas que puede elegir para mutar
        Las filas se muestran segun el sentido elegido
        """
        matriz = [
            ["------", "------", "------", "Fila:1", "Fila:2", "Fila:3"],
            ["------", "------", "Fila:1", "Fila:2", "Fila:3", "Fila:4"],
            ["------", "Fila:1", "Fila:2", "Fila:3", "Fila:4", "Fila:5"],
            ["Fila:1", "Fila:2", "Fila:3", "Fila:4", "Fila:5", "------"],
            ["Fila:2", "Fila:3", "Fila:4", "Fila:5", "------", "------"],
            ["Fila:3", "Fila:4", "Fila:5", "------", "------", "------"]
        ]
        if self.direccion == 1:# Sentido ascente
            self.separar()
            print("\n".join("  ".join(matriz[i][j] for j in range(6)) for i in range(6)))
        else:
            # Sentido descendente
            matriz = self.revertir(matriz) # Se revierte la matriz
            self.separar()
            print("\n".join("  ".join(matriz[i][j] for j in range(6)) for i in range(6)))

    def revertir(self,matriz: list) -> list:
        """
        Método que retorna una versión revertida de las sublistas de la matriz
        """
        return [list(reversed(sublista)) for sublista in matriz]

    def elegir_filas(self) -> list:
        """
        Se le pide al usuario que igrese la fila que desea mutar
        Si el input corresponde al formato retornara e imprimira
        las coordenadas de los elementos de la fila dependiendo
        el sentido (self.direccion)
        """
        while True:# Se verifica que el usuario ingrese de forma correta el input
            fila  = input("\nIngrese el número de la fila seleccionada: ")
            # Se verfica que la entrada corresponda a las claves del diccionario de coordenadas
            if fila in self.coordenadas.keys() and len(fila) == 1 :
                break
            else:
                print("Ingreso incorrecto, siga el formato")
        # Retorna el valor de la clave introducida segun el sentido, la clave es una lista con coordendass
        if self.direccion == 1: # Ascendente
            print(f"Has seleccionado la {fila}. Coordenadas: {self.coordenadas[fila]}")
            return self.coordenadas[fila]
        else:
            # Descendente
            coordenadas = list(reversed(self.coordenadas[fila])) # Revierte la lista de coordenadas
            print(f"Has seleccionado la {fila}. Coordenadas: {coordenadas}")
            return coordenadas

    def crear_mutante(self,adn: list,base: str,direccion: int) -> list:
        self.adn = adn
        self.base = base
        self.direccion = direccion
        """
        Método heredado modificado
        Mientras se respete el fomato este método retorna una matriz modificada
        en caso contrario se le pedira al usuario que lo intente de nuevo
        """
        while True:
            try:
                self.separar()
                print("\nElija donde quiere generar el mutante diagonal")
                print("Mutante Ascendente") if self.direccion == 1 else print("\nMutante Descendente")# Muestra la dirección del usuario
                self.mostrar_coordenadas()
                self.separar()
                # Se llama al método para determinar con que coordenadas trabajar
                secuencia =self.elegir_filas()

                # Pedir las coordenadas desde donde se inicia la mutación
                origen = list(input("\nIngrese un par de coordenadas en forma de decena (fila, columna. Ej: [2,1] = 21): "))
                origen = list(map(int, origen))
                if origen not in secuencia and len(origen) != 2:# Se crea una instancia de error si se la entrada es diferente al formato
                    raise ValueError("\nIngrese solamente el par de coordenadas dentro de la fila")
                inicio = secuencia.index(origen)# Se guarda el indice perteneciente al origen introducido
                
                # Cambia los valores de las coordenadas de la matriz por la base ingresada por el usuario
                for i in range(self.cantidad):
                    fila, columna = secuencia[inicio + i]
                    self.adn[fila][columna] = self.base
                
                # Según la dirección se invierte la matriz o no
                if self.direccion == 1:
                    return self.adn
                else:
                    adn = self.adn
                    return self.revertir(adn)# Retorna una versión revertida de la matriz

                # Razones para pedir al usuario que lo intente devuelta
            except ValueError as error:# Ingresar mal los datos
                self.limpiar_consola()
                self.separar()
                print(f"\nError. {error}")
            except IndexError:# Ingresar un origen que produzca iterar fuera de la matriz
                self.limpiar_consola()
                self.separar()
                print("\nError: Fuera de rango de la matriz | RECUERDE: la base se repite 4 veces dentro del rango de la fila")