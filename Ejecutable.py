import Clases
import os

def limpiar_consola():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas Unix (Linux/macOS)
        os.system('clear')

def imprimir_secuencia(adn):
    print("\n".join("  ".join(adn[i][j] for j in range(6)) for i in range(6)))
    print("")

def verificar_opciones(mensaje,opciones):
    while True:
        try:
            option = int(input(mensaje))
            if option in opciones:
                return option
            else:
                print("Intentelo nuevamente")
        except ValueError:
            print("Por favor ingrese un número válido.")

def mutar(adn):
    pass

def sanar(adn):
    adn1 = Clases.Sanador(adn)
    adn = adn1.sanar_mutantes()
    imprimir_secuencia(adn)
    return adn

def detectar(adn):
    adn1 = Clases.Detector(adn)
    if adn1.detectar_mutantes() == True:
        print("La secuencia de ADN contiene mutaciones")
        print("")
        option = verificar_opciones("Que aciones tomara? Mutar ADN: 1 | Sanar ADN: 2|:  ", (1,2))
        print("")
        if option == 1:
            adn = mutar(adn)
            return adn
        else:
            adn = sanar(adn)
            return adn
    else:
        print("Esta secuencia no contiene mutaciones")
        return adn


while True:
    adn = [] 
    BASES_NITROGENADAS = ["A","C","G","T"]
    TAM_SECUENCIA = 6

    print("Para empezar tendra que incertar una secuencia de ADN")
    print("Si coloca mal alguna secuencia de bases, se le pedira que la ingrese devuelta")

    for i in range(TAM_SECUENCIA):# Bucle de de input de secuencia
        while True:# Bucle de verificación de input de secuencia
            secuencia = input(f"Ingrese la {i+1}º secuencia de 6 bases nitrogenadas: ").upper()
            if len(secuencia) == TAM_SECUENCIA and all(base in BASES_NITROGENADAS for base in secuencia):
                adn.append(list(secuencia))
                break
            else:
                print("Intentelo nuevamente. Secuencia Invalida")
    print("")

    print("Esta es la secuecia de ADN que usted ingreso")
    print("")
    imprimir_secuencia(adn)
    print("------------------------------------")

    while True:
        print("Que es lo que desea hacer?")
        option = verificar_opciones("Detectar mutantes: 1 | Mutar ADN: 2 | Sanar ADN: 3|:  ", (1,2,3))

        if option == 1:
            adn = detectar(adn)
            
        elif option == 2:
            adn = mutar(adn)
        else:
            adn = sanar(adn)
            
        option = verificar_opciones("Quiere seguir usando esta secuenciade ADN | Si: 1 | No: 2 | :  ", (1,2))
        print("")
        if option == 1:
            break
        else:
            pass
    print("------------------------------------")
    print("Quiere salir o continuar con otra secuencia de AND?")
    option = verificar_opciones("Salir del programa? Si: 1 | No: 2 | :  ", (1,2))
    print("") 
    if option == 1:
        break
    else:
        limpiar_consola()







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