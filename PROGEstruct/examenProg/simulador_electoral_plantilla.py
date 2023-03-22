"""
El Ministerio del Interior está preparando la infraestructura para las elecciones municipales de mayo de 2023 y ha
contactado con el IES Gran Capitán para que le hagamos un simulador de resultados electorales municipales, ya que
sospecha que alguno de sus sistemas ha podido ser atacado y no se acaba de fiar de la veracidad de los datos.

La ley electoral dice que para poder tener representación en un municipio hay que superar el 5% de los votos válidos y
el reparto de escaños se hace mediante la Ley D'Hondt.

Con el propósito de testear mejor el programa se incluye una opción que carga los resultados electorales municipales de
Córdoba de 2019.
"""
from utilities import menu

MIN_PERCENT_VOTES = 0.05

city = None
valid_votes = 0
seats = 0
votes_parties = []


def main():
    condition_to_input = False
    while True:
        option = menu("Simulador electoral municipal", "Cargar datos de las elecciones municipales de Córdoba de 2019",
                      "Introducir datos electorales", "Introducir partido y votos", "Ver simulación", "Finalizar")

        if option == 1:
            load_electoral_data_cordova()
            condition_to_input = True
        elif option == 2:
            input_electoral_data()
            condition_to_input = True
        elif option == 3:
            if condition_to_input:
                input_party_votes()
            else:
                print('ERROR. Para ejecutar la tercera opción hay que ejecutar primero la primera o segunda opción.')
                continue
        elif option == 4:
            if condition_to_input:
                print_simulation()
            else:
                print('ERROR. Para ejecutar la cuarta opción hay que ejecutar primero la primera o segunda opción.')
                continue
        else:
            break
        print()

    print("¡Hasta la próxima! ;-)")


def load_electoral_data_cordova():
    global city, valid_votes, seats, votes_parties
    city = "CÓRDOBA"
    valid_votes = 146548
    seats = 29
    votes_parties = [[43434, "PP"], [36169, "PSOE"], [22094, "Ciudadanos"], [15656, "IU ANDALUCÍA"],
                     [11788, "VOX"], [9144, "PODEMOS"], [1653, "PACMA"], [951, "ACCIÓN POR CÓRDOBA"],
                     [380, "PCTE"], [360, "ANDALUCÍA ENTRE TOD@S"], [320, "GANEMOS"], [320, "EB"],
                     [161, "PUM+J"]]
    print("Datos de Córdoba cargados.")


def input_electoral_data():
    global city, valid_votes, seats, votes_parties

    option = input('Esto implica borrar los datos ya introducidos. Responda "Sí" para proceder: ')
    if option == 'Sí':
        city = input('Municipio: ')
        valid_votes = int(input('Votos válidos: '))
        seats = int(input('Número de ediles: '))
    pass


def party_not_inserted_exception(party):
    for i in votes_parties:
        if party in votes_parties:
            return True
        else:
            break


def votes_max_exception(votes):
    pass


def input_party_votes():
    global city, valid_votes, seats, votes_parties
    party = input('Partido político: ')
    party_not_inserted_exception(party)
    got_votes = int(input('Número de votos obtenido: '))
    votes_max_exception(got_votes)
    return votes_parties


def print_simulation():
    global city, valid_votes, seats, votes_parties
    pass


if __name__ == "__main__":
    main()
