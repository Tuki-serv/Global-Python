"""def mal_input(i,b):
    while True:
        secuencia = input(f"Ingrese nuevamente la {i+1}º secuencia de 6 bases nitrogenadas: ")
        correccion = list(secuencia)
        if len(correccion) == 6 and all(base in b for base in correccion):
            break
    return correccion
"""
import Clases

adn = [] 
BASES_NITROGENADAS = ["A","C","G","T"]

print("Para empezar tendra que incertar una secuencia de ADN")
print("Si coloca mal alguna secuencia de bases, se le pedira que la ingrese devuelta")
TAM_SECUENCIA = 6
for i in range(TAM_SECUENCIA):
    while True:
        secuencia = input(f"Ingrese la {i+1}º secuencia de 6 bases nitrogenadas: ").upper()
        if len(secuencia) == TAM_SECUENCIA and all(base in BASES_NITROGENADAS for base in secuencia):
            adn.append(list(secuencia))
            break
        else:
            print("Intentelo nuevamente. Secuencia Invalida")
print("")

print("Esta es la secuecia de ADN que usted ingreso")
for i in range (6):
    for j in range (6):
        print(f"{adn[i][j]}", end=" ")
    print("")

adn1= Clases.Detector(adn)

input()
"""
ACGTAC
TGCATG
GATCGA
ATGCAT
CGATCG
TAGCTA
"""