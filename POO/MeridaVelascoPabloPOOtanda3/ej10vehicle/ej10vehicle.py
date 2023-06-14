"""
10. Crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera. Para la clase Vehicle,
genera los atributos de clase vehicles_created y total_kilometers, así como el atributo de instancia kilometers_traveled.

En la clase Vehicle genera un método para viajar (travel) que incremente los kilómetros recorridos. En la clase Bike haz
un método para hacer el caballito y en la clase Car otro para quemar rueda.

Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como el que se
muestra a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Ver kilometraje de la bicicleta
6. Ver kilometraje del coche
7. Ver kilometraje total
8. Salir

"""
from abc import ABC

from menu import Menu


def total_vehicles_km():
    return f'Los vehículos almacenados han recorrido: {Vehicle.total_kilometers}'


class Vehicle(ABC):
    total_kilometers = 0
    vehicle_created = 0

    def __init__(self, name: str, kilometers_traveled: int):
        self.km = kilometers_traveled
        self.__name = name
        Vehicle.vehicle_created += 1

    @property
    def name(self):
        return self.__name

    @property
    def km(self):
        return f'{self.__name} ha recorrido {self.__km} kilómetros'

    @km.setter
    def km(self, value):
        self.__km = value

    def travel(self, distance):
        self.__km += distance
        Vehicle.total_kilometers += self.__km
        return f'{self.__class__.__name__}: Acaba de recorrer {self.__km} kilómetros.'

    def total_km(self):
        return f'{self.__name} ha recorrido {self.__km} kilómetros'


class Bike(Vehicle):

    def wheelie(self):
        return f'{self.__name}: Pedazo caballitooooo!!!'


class Car(Vehicle):

    def burn_wheel(self):
        return f'{self.__name}: Quemando esas gomass!!!'


if __name__ == '__main__':
    menu = Menu('Vehículos', 'Anda con la bicicleta', 'Haz el caballito con la bicicleta', 'Anda con el coche',
                'Quema rueda con el coche', 'Ver kilometraje de la bicicleta', 'Ver kilometraje del coche',
                'Ver kilometraje total', 'Salir')

    bike1 = Bike('Merida 4080', 30)
    car1 = Car('Honda Civic', 8000)

    while True:
        opt = menu.choose()
        match opt:
            case 1:
                bike1.travel(5)
            case 2:
                bike1.wheelie()
            case 3:
                car1.travel(25)
            case 4:
                car1.burn_wheel()
            case 5:
                bike1.total_km()
            case 6:
                car1.total_km()
            case 7:
                total_vehicles_km()
            case _:
                print('Hasta la próxima.')
                break
