import random
import os

class Detector:
    # Clase para detectar secuencias mutantes en una matriz de ADN.
    
    # Constantes para la detección de mutantes
    CANTIDAD_MAXIMA = 3  # Máximo de bases iguales consecutivas permitidas
    rango_secuencia = 6  # Tamaño de las secuencias en la matriz (6x6)
    coordenadas = {  # Coordenadas para detectar secuencias diagonales
        "d1": [(3, 0), (2, 1), (1, 2), (0, 3)],
        "d2": [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
        "d3": [(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)],
        "d4": [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)],
        "d5": [(5, 2), (4, 3), (3, 4), (2, 5)]
    }

    def __init__(self, adn: list) -> None:
        # Inicializa la matriz de ADN y un contador para bases consecutivas.
        self.adn = adn
        self.contador = 1

    def detectar_mutantes(self) -> bool:
        # Método principal que verifica si existen mutaciones.
        return self.mutantes()

    def mutantes(self) -> bool:
        # Verifica secuencias mutantes en todas las direcciones: horizontal, vertical y diagonal.
        return any(self.direcciones(direccion) for direccion in ["horizontal", "vertical", "diagonal", "diagonal.invertida"])

    def verficacion(self, lista: list, rango: int) -> bool:
        # Verifica si una lista contiene más de 3 bases iguales consecutivas.
        self.identidad = lista
        for j in range(1, rango):
            if self.identidad[j] == self.identidad[j-1]:
                self.contador += 1  # Incrementa el contador si las bases consecutivas son iguales.
            else:
                self.contador = 1  # Reinicia el contador si no son iguales.
            if self.contador > self.CANTIDAD_MAXIMA:
                return True
        return False

    def direcciones(self, direccion: str) -> bool:
        # Genera listas de secuencias según la dirección especificada y las verifica.
        if direccion == "horizontal":
            secuencias = [self.adn[fila] for fila in range(self.rango_secuencia)]
        elif direccion == "vertical":
            secuencias = [[self.adn[fila][columna] for fila in range(self.rango_secuencia)] for columna in range(self.rango_secuencia)]
        elif direccion == "diagonal":
            secuencias = self.diagonales(1)
        elif direccion == "diagonal.invertida":
            secuencias = self.diagonales(2)
        return any(self.verficacion(secuencia, len(secuencia)) for secuencia in secuencias)

    def diagonales(self, control: int) -> list:
        # Genera listas con las diagonales de la matriz (ascendentes y descendentes).
        if control == 1:
            return [[self.adn[x][y] for x, y in coords] for coords in self.coordenadas.values()]
        else:
            matriz_invertida = [list(reversed(fila)) for fila in self.adn]
            return [[matriz_invertida[x][y] for x, y in coords] for coords in self.coordenadas.values()]

class Sanador(Detector):
    # Clase que corrige las secuencias mutantes generando una nueva matriz.

    __BASES_NITROGENADAS = ["A", "C", "G", "T"]

    def sanar_mutantes(self) -> list:
        # Corrige la matriz si se detectan mutaciones.
        if self.detectar_mutantes():
            print("\nLa secuencia de ADN contiene mutaciones, comienza la curación.")
            while True:
                # Genera una nueva matriz aleatoria hasta que no se detecten mutaciones.
                self.adn = [[random.choice(self.__BASES_NITROGENADAS) for _ in range(self.rango_secuencia)] for _ in range(self.rango_secuencia)]
                if not self.detectar_mutantes():
                    print("\nSecuencia curada con éxito.")
                    return self.adn
        print("\nLa secuencia de ADN no contiene mutaciones.")
        return self.adn

class Mutador:
    # Clase base para mutar la matriz de ADN, utilizada por subclases.

    def __init__(self) -> None:
        self.cantidad = 4  # Número de bases consecutivas para una mutación
        self.coordenadas = {  # Coordenadas diagonales
            "fila:1": [[3, 0], [2, 1], [1, 2], [0, 3]],
            "fila:2": [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]],
            "fila:3": [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]],
            "fila:4": [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],
            "fila:5": [[5, 2], [4, 3], [3, 4], [2, 5]]
        }

    def limpiar_consola(self) -> None:
        # Limpia la consola según el sistema operativo.
        os.system('cls' if os.name == 'nt' else 'clear')

class Radiacion(Mutador):
    # Subclase que muta la matriz en sentido horizontal o vertical.

    def crear_mutante(self, adn: list, base: str, direccion: int) -> list:
        # Realiza una mutación en sentido horizontal o vertical.
        while True:
            try:
                print("\nElija donde quiere generar el mutante")
                origen = input("Ingrese la coordenada inicial (Fila, Columna. Ej: 21): ")
                if len(origen) != 2:
                    raise ValueError("Formato inválido. Use dos números seguidos.")
                fila, columna = map(int, origen)
                
                indices = [(fila, columna + i) for i in range(self.cantidad)] if direccion == 1 else [(fila + i, columna) for i in range(self.cantidad)]
                
                for x, y in indices:
                    adn[x][y] = base
                print("\nMutante creado.")
                return adn
            except (ValueError, IndexError) as error:
                print(f"\nError: {error}. Intente nuevamente.")

class Viruz(Mutador):
    # Subclase que muta la matriz en sentido diagonal (ascendente o descendente).

    def crear_mutante(self, adn: list, base: str, direccion: int) -> list:
        # Realiza una mutación en sentido diagonal.
        while True:
            try:
                secuencia = self.coordenadas["fila:1"]  # Ejemplo para simplificar lógica
                for i in range(self.cantidad):
                    fila, columna = secuencia[i]
                    adn[fila][columna] = base
                print("\nMutante creado.")
                return adn
            except Exception as error:
                print(f"\nError: {error}. Intente nuevamente.")
