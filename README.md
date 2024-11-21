# Project-Mutant

Bienvenido!! Estamos felices de que forme parte de la comunidad de **Project_Mutant** 
Nosotros somos :
## Instrucciones:
### Para empezar :
- Para usar nuestro programa, le pedimos que ingrese una secuencia de ADN
- Deberá saber que la secuencia de ADN será representada visualmente por una matriz
- La secuencia debe ser ingresada en subsecuencias de seis bases nitrogenadas
- Las bases nitrogenadas son : 
  -  Adenina (A), Timina (T), Citosina (C) y Guanina (G)


### Como interactuar con la secuencia de ADN
#### Detectar Mutantes en el ADN
Realiza una búsqueda de mutaciones en la secuencia de ADN, se considera mutación cuando una base nitrogenada se repite más de 3 tres veces en alguna dirección de la secuencia del ADN.
#### Mutar ADN
   Genera una mutación en la secuencia de ADN. Se le pedirá que ingrese una base nitrogenada la cual generara el mutante, luego se le pregunta la dirección de la mutación
   Tenga en cuenta que la mutación será producida por una base nitrogenada repetida 4 veces 
   Direcciones Horizontal y Vertical: 
   - Se le pedirá que ingrese las coordenadas de origen en formato de decena 
   - Fila, Columna.
   - Ejemplo:
     - Fila: 0 | Columna 1 = 01 
     - Fila: 2 | Columna 3 = 23

| 00  | 01  | 02  | 03  | 04  | 05  |
| --- | --- | --- | --- | --- | --- |
| 10  | 11  | 12  | 13  | 14  | 15  |
| 20  | 21  | 22  | 23  | 24  | 25  |
| 30  | 31  | 32  | 33  | 34  | 35  |
| 40  | 41  | 42  | 43  | 44  | 45  |
| 50  | 51  | 52  | 53  | 54  | 55  |

Direcciones Diagonales: Ascendente y Descendente:
- Se le pedirá que ingrese la orientación y luego deberá ingresar la fila donde desea mutar
- Se le mostraran las coordenadas de esa fila y se le pedirá que las ingrese en el mismo formato de las direcciones Horizontal y Vertical
#### Sanar ADN
Si detecta mutaciones, generara una nueva secuencia de ADN de forma aleatoria, mostrándola por la pantalla
###  Para terminar
- Se le preguntara si desea seguir usando la secuencia de ADN generada (ya sea la secuencia mutada o la sanada) para interactuar con ella
- En caso de no seguir usando la secuencia de ADN se le preguntara si desea salir o continuar con otra secuencia de ADN
## Secuencias a modo de ejemplo

| Secuencia Normal                                         | Mutación Horizontal                                          | Mutación Vertical                                                        | Mutación Diagonal Descendente                                            | Mutación Diagonal Ascendente                                                 |
| -------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| ACGTAC<br>TGCATG<br>GATCGA<br>ATGCAT<br>CGATCG<br>TAGCTA | ACGTAC<br>TGCATG<br>GATCGA<br>ATGCAT<br>CGATCG<br>T**AAAA**G | ACGTAG<br>TGCATT<br>GATCG**C**<br>ATGCA**C**<br>CGATC**C**<br>TAGCT**C** | **T**GATCA<br>G**T**TTCA<br>CA**T**CAT<br>GAG**T**TA<br>ATTGCG<br>CTGTTC | ACGT**A**C<br>CGA**A**CA<br>TG**A**CCT<br>G**A**TACA<br>**A**CAGGA<br>GTTCAT |
# Integrantes 

## Juan Cruz Ana
## Jonathan Serrano Ojeda
## Santiago Rubén Sordi
## Lucas Gonzalo Hernández 