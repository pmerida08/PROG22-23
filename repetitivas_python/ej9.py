"""
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

Autor: Pablo Mérida Velasco
Fecha: 25/10/2022
"""

print('Este programa calcula los N primeros numeros.')
print('---------------------------------------------')

N = 10  # cantidad de primos

print("2")  # Primer primo y único primo par

candidato_a_primo = 3  # Número posible que puede ser primo
total_primos_mostrados = 1  # Cuantos números hemos mostrado para parar el programa

while total_primos_mostrados < N:   # Mientras que no hayamos impreso la cantidad de primos pedida hacemos:
    # Vemos si el candidato es primo
    es_primo = True
    for divisor in range(3, int(candidato_a_primo ** 0.5) + 1, 2):  # Comprobamos solo hasta la raíz cuadrada del
        # candidato, de dos en dos
        if candidato_a_primo % divisor == 0:
            es_primo = False
            break

    # Si el candidato es primo lo muestro
    if es_primo:
        print(candidato_a_primo)
        total_primos_mostrados += 1

    candidato_a_primo += 2  # Siguiente candidato
