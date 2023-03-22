"""
Ejercicio 3:
Este programa juega a piedra/papel/tijera contra el ordenador que usa números aleatorios para realizar la tirada.
Después de cada jugada pregunta al usuario si quiere continuar, en caso negativo se muestra el número de
partidas jugadas, las ganadas por cada jugador y las empatadas.

"""

import random

print('Este programa hace el juego de piedra papel o tijera.')
total_matches = 0
matches_won = 0
matches_draw = 0
matches_lost = 0

while True:
    computer_choose = random.randint(0, 2)
    human_choose = int(input('¿Qué tira el usuario piedra, papel, o tijeras? [0/1/2]: '))

    match human_choose:
        case 0:
            if computer_choose == 0:
                print('Has sacado lo mismo que la IA')
                matches_draw += 1
                total_matches += 1
            elif computer_choose == 1:
                print('Has perdido la partida: piedra pierde contra papel')
                matches_lost += 1
                total_matches += 1
            else:
                print('Has ganado la partida: piedra gana a tijeras.')
                matches_won += 1
                total_matches += 1
        case 1:
            if computer_choose == 0:
                print('Has ganado la partida: papel gana contra piedra')
                matches_won += 1
                total_matches += 1
            elif computer_choose == 1:
                print('Has sacado lo mismo que la IA')
                matches_draw += 1
                total_matches += 1
            else:
                print('Has perdido la partida: papel pierde contra tijeras.')
                matches_lost += 1
                total_matches += 1
        case 2:
            if computer_choose == 0:
                print('Has perdido la partida: tijera pierde contra piedra.')
                matches_lost += 1
                total_matches += 1
            elif computer_choose == 1:
                print('Has ganado la partida: tijera pierde contra papel')
                matches_won += 1
                total_matches += 1
            else:
                print('Has sacado lo mismo que la IA')
                matches_draw += 1
                total_matches += 1

    keep_playing = input('¿Desea seguir jugando?(Si/No): ')
    if keep_playing == 'Si':
        continue
    else:
        break

print('---------------------------------------------')
print('Las partidas ganadas son: ', matches_won)
print('Las partidas empatadas son: ', matches_draw)
print('Las partidas perdidas son: ', matches_lost)
print('El total de partidas es: ', total_matches)
