"""
1. Implementa el control de acceso al área restringida de un programa. Se debe pedir un nombre de usuario y una
contraseña. Si el usuario introduce los datos correctamente, el programa dirá “Ha accedido al área restringida”. El
usuario tendrá un máximo de 3 oportunidades. Si se agotan las oportunidades el programa dirá “Lo siento, no tiene
acceso al área restringida”. Los nombres de usuario con sus correspondientes contraseñas deben estar almacenados en un
diccionario.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 05/03/2023
"""
from typeguard import typechecked

MAX_ATTEMPTS = 3

@typechecked
class User:

    users = {}

    def __init__(self, user: str, passw: str):
        self.__user = user
        self.__passw = passw

    def register(self):
        User.users[self.__user] = self.__passw

    @staticmethod
    def login():
        attempts = 0
        while attempts < MAX_ATTEMPTS:
            attempts += 1
            user1 = User.input_users()
            if attempts == MAX_ATTEMPTS: return f'Lo siento, no tiene acceso al área restringida'
            if User.check(user1):
                return 'Has accedido al área restringida.'
            else:
                print(f'Intento {attempts}: Usuario o contraseña incorrecto, inténtalo otra vez')

    @staticmethod
    def input_users():
        user = input('Introduce el usuario: ')
        passw = input('Introduce la contraseña: ')
        user1 = User(user, passw)
        return user1

    @staticmethod
    def check(other: 'User'):
        for user_i, passw_i in User.users.items():
            if other.__user == user_i and other.__passw == passw_i:
                return True
        return False

    def __str__(self):
        return f"Usuario: {self.__user}     |    Contraseña: {self.__passw}"

    def __repr__(self):
        return f"Usuario: {self.__user}     |    Contraseña: {self.__passw}"

if __name__ == '__main__':
    user_reg1 = User('Lola', '34')
    user_reg2 = User('Jose', 'Maria')
    User.register(user_reg1)
    User.register(user_reg2)
    print(User.users)
    print(User.login())
