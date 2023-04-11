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
            if option != election:
                print(f'La puntuación obtenida es de {self.__base_pointed*points} puntos')
                break
            elif option == election:
                print(f'La puntuación obtenida es de {self.__base_pointed*points} puntos')
                break

    def show(self):
        print(f'Pregunta {Question.__number_quests}. {self.__enunciate}')
        for election in self.__elections:
            print(f"- {election[0]}")

if __name__ == '__main__':
    q1 = Question('q1', '¿Qué son los mamíferos?',
                [('Seres vivos', 2), ('Plantas', -0.25), ('Insectos', -0.25), ('Partido político', -0.25)], 1)
    q1.show()
    q1.answer()

    q2 = Question('q2', '¿En qué nivel evoluciona Totodile en Croconaw?',
                [('16', -0.25), ('18', 2), ('17', -0.25), ('19', -0.25)], 1)
    q2.show()
    q2.answer()

