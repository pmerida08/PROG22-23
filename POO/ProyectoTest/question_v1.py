from typeguard import typechecked

@typechecked
class Question:
    __BASE_POINTS_MAX = 2
    __number_quests = 0

    def __init__(self, name: str, enunciate: str, elections: list[tuple[str, float]], base_pointed: int):
        self.__name = name
        self.__enunciate = enunciate
        self.__elections = elections
        self.__base_pointed = base_pointed
        Question.__number_quests += 1

    @property
    def enunciate(self):
        return self.__enunciate

    @property
    def elections(self):
        return self.__elections

    def answer(self):
        election = input('Indique la opción correcta: ')
        if election == '':
            print(f'La puntuación obtenida es de 0 puntos')
        for option, points in self.__elections:
            if option == election:
                score = self.__base_pointed*points
                print(f'La puntuación obtenida es de {score} puntos \n')

    def show(self):
        print(f'Pregunta {Question.__number_quests}. {self.__enunciate}')
        for election in self.__elections:
            print(f"- {election[0]}")

if __name__ == '__main__':
    q1 = Question('q1', '¿Qué son los mamíferos?',
    [('Seres vivos', 2), ('Plantas', -0.25), ('Insectos', -0.25), ('Partido político', -0.25)], 1)
    q1.show()
    q1.answer()

    q2 = Question('q2', '¿En qué meridiano está España?',
    [('M. magnético', -0.25), ('M. de Greenwich', 2), ('M. cero', -0.25), ('Ecuador', -0.25)], 1)
    q2.show()
    q2.answer()

    q3 = Question('q3', '¿Cuál es la capital de Marruecos?',
    [('Ceuta', -0.25), ('Melilla', -0.25), ('Rabat', 2), ('Marrakech', -0.25)], 1)
    q3.show()
    q3.answer()

    q4 = Question('q4', '¿En qué año murió Francisco Franco?',
    [('1976', -0.25), ('1973', -0.25), ('1978', -0.25), ('1975', 2)], 1)
    q4.show()
    q4.answer()

    q5 = Question('q5', '¿Cuál fue el primer programador/a?',
    [('Ada Lovelace', 2), ('von Neumann', -0.25), ('Peter Griffin', -0.25), ('Bill Gates', -0.25)], 1)
    q5.show()
    q5.answer()
