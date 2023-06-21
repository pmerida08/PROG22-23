from typeguard import typechecked


class QuestionError(Exception):
    def __init__(self, msg):
        super().__init__(f'Error: {msg}')
        self.__msg = msg


class QuestionResponseError(QuestionError):
    def __init__(self, response):
        super().__init__(f'La respuesta {response} no se corresponde con ninguna de las opciones')
        self.__response = response


@typechecked
class Question:

    def __init__(self, name: str, enunciate: str, elections: list[tuple[str, float]], base_pointed: int = 1):
        self.__name = name
        self.__enunciate = enunciate
        self.__elections = elections
        self.__base_pointed = base_pointed

    @property
    def name(self):
        return self.__name

    @property
    def enunciate(self):
        return self.__enunciate

    @property
    def elections(self):
        return self.__elections

    @property
    def base_pointed(self):
        return self.__base_pointed

    def get_points(self, response):
        if response > len(self.__elections) or response < 0:
            raise QuestionResponseError(response)
        return self.__elections[response - 1][1]
