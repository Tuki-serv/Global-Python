import Clases
import os

def limpiar_consola() -> None:
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas Unix (Linux/macOS)
        os.system('clear')

def separar() -> None:
    """
        Este método crea una línea para separar
        se creo para mas facilidad en el uso
        """
    print("----------------------------------------------")

def imprimir_secuencia(adn: list) -> None:
    """
    Imprime la matriz(secuencia ADN) ingresada
    """
    print("\n".join("  ".join(adn[i][j] for j in range(6)) for i in range(6)))
    print("")

def verificar_opciones(mensaje:str ,opciones: tuple,limite: int) -> int:
    """
    Verifica los inputs del usuario
    """
    while True:# Si se ingresa un valor incorreto se le pide que lo intente devuelta
        try:
            option = input(mensaje)
            # Verifica que el input corresponda a algún elemento de opciones
            if option in opciones and len(option) == limite:
                return int(option)
            else:
                separar()
                print("\nIntentelo nuevamente")
        except ValueError:# Entrada no valida
            separar()
            print("\nPor favor ingrese un número válido.")

def mutar(adn: list) -> list:
    """
    Función encargada de instanciar objetos
    en la clases mutantes(Radiación, Viruz)
    Guarda el retorno del objeto
    dentro de una variable para su uso posterior
    """
    while True:# Si se ingresa un valor incorreto se le pide que lo intente devuelta
        base = input("Ingrese la base nitrogenada que desea que genera la mutación: ").upper()
        if base in BASES_NITROGENADAS:# Se verifica si el input pertenece a las bases
            break
        else:
            separar()
            print("\nIntentelo nuevamente.")

    # Se le pregunta al usuario que medidas quiere tomar
    option = verificar_opciones("\nComo queres mutar? \nHorizontal:1 \nVertical:2 \nDiagonal:3 | :  ", ("1","2","3"),1)# Llamada a la función
    
    if (option == 1) or (option == 2):
        adn1 = Clases.Radiacion()# Se crea un objeto en la Clase Radiación
        adn = adn1.crear_mutante(adn,base,option)# Se guarda la matriz
        imprimir_secuencia(adn)# Se imprime la matriz
        return adn# Retorna la matriz
    else:
        print("\nEn que sentido queres generar el mutante?")
        sentido = verificar_opciones("Ascendente: 1 | Descendente: 2 | : ",("1","2"),1)
        adn1 = Clases.Viruz()# Se crea un objeto en la Clase Viruz
        adn = adn1.crear_mutante(adn,base,sentido)# Se guarda la matriz
        imprimir_secuencia(adn)# Se imprime la matriz
        return adn# Retorna la matriz

def sanar(adn: list) -> list:
    """
    Función encargada de instanciar objetos
    en la Clase Sanador
    Guarda el retorno del objeto 
    dentro de una variable para su uso posterior
    """
    adn1 = Clases.Sanador(adn)# Se crea un objeto en la Clase Sanador
    adn = adn1.sanar_mutantes()# Se guarda la matriz
    imprimir_secuencia(adn)# Se imprime la matriz
    return adn# Retorna la matriz

def detectar(adn: list) -> list:
    """
    Función encargada de instanciar objetos
    en la Clase Detector
    Toma acciones dependiendo el retorno del método(detectar_mutantes)
    """
    adn1 = Clases.Detector(adn)
    # Acciones a tomar segun el retorno (detectar_mutantes)
    if adn1.detectar_mutantes() == True:
        print("\nLa secuencia de ADN contiene mutaciones\n ")
        
        # Se le pregunta al usuario que medidas quiere tomar
        option = verificar_opciones("\nQue aciones tomara? Mutar ADN: 1 | Sanar ADN: 2|:  ", ("1","2"),1)# Llamada a la función
        if option == 1:
            adn = mutar(adn)# Llamada a la función
            return adn# Se retorna la matriz
        else:
            adn = sanar(adn)# Llamada a la función
            return adn# Se retonra la matriz
    else:
        # Si el método(detectar_mutantes) retorna falso
        print("\nEsta secuencia no contiene mutaciones")
        return adn# Se retorna la función

while True:# Segun quiera el usuario, se cierra el programa
    adn = [] # Secuencia de ADN (matriz)
    BASES_NITROGENADAS = ["A","C","G","T"] # Bases que se utilizan
    TAM_SECUENCIA = 6 # Tamaño de la matriz 6x6

    print("\nPara empezar tendra que incertar una secuencia de ADN")
    print("Si coloca mal alguna secuencia de bases, se le pedira que la ingrese devuelta")
    print("Bases nitrogenadas: A C G T")
    # Se crea una lista con la entrada del usuario
    for i in range(TAM_SECUENCIA):# Bucle de input de secuencia
        while True:# Bucle de verificación de input de secuencia
            secuencia = input(f"Ingrese la {i+1}º secuencia de 6 bases nitrogenadas: ").upper()
            
            if len(secuencia) == TAM_SECUENCIA and all(base in BASES_NITROGENADAS for base in secuencia):
                adn.append(list(secuencia))# Se agrega la lista a la matriz
                break # Se sale del bucle
            else:
                # Se le pide que ingrese devuelta la secuencia
                separar()# Llamada a la función
                print("\nIntentelo nuevamente. Ingrese una secuencia valida")
    limpiar_consola()# Llamada a la función

    # Se le muestra al usuario la secuencia de ADN (matriz)
    print("\nEsta es la secuecia de ADN que usted ingreso")
    imprimir_secuencia(adn)# Llamada a la función
    separar()# Llamada a la función

    # Se le pregunta al usuario que acción tomar
    while True:
        print("Que es lo que desea hacer?")
        option = verificar_opciones("Detectar mutantes: 1 | Mutar ADN: 2 | Sanar ADN: 3|:  ", ("1","2","3"),1)# Llamada a la función

        # Como interactuar con la matriz
        if option == 1:
            adn = detectar(adn)# Llamada a la función
        elif option == 2:
            adn = mutar(adn)# Llamada a la función
        else:
            adn = sanar(adn)# Llamada a la función

        # Se le pregunta si quiere seguir usando la matriz 
        option = verificar_opciones("Quiere seguir usando esta secuenciade ADN | Si: 1 | No: 2 | :  ", ("1","2"),1)# Llamada a la función
        print("")
        if option == 1:
            # Se le mostrara al usuario devuelta como interactuar con la matriz
            limpiar_consola()# Llamada a la función
            print("\nEsta es la secuencia de ADN que esta usando")
            imprimir_secuencia(adn)# Llamada a la función
            pass
        else:
            break
    limpiar_consola()# Llamada a la función

    # Se le pregunta si quiere cerrar el programa o introducir una nueva matriz
    print("\nQuiere salir o continuar con otra secuencia de AND?")
    option = verificar_opciones("Salir del programa? Si: 1 | No: 2 | :  ", ("1","2"),1)# Llamada a la función
    if option == 1:# Salir programa| Sale del bucle infinito
        break
    else:
        # Se reinician todos los datos del programa para un nuevo uso
        limpiar_consola()# Llamada a la función







"""
ACGTAC
TGCATG
GATCGA
ATGCAT
CGATCG
TAGCTA
"""
"""
TGATCA
GTTTCA
CATCAT
GAGTTA
ATTGCG
CTGTTC
"""
