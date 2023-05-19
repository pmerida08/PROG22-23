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
