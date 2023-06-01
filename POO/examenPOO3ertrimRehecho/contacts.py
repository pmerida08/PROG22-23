import re
from typeguard import typechecked

PATH_MAIL = r'[^@\t\r\n]+@[^@\t\r\n]+\.[^@\t\r\n]+'

PATH_NUMBER = r'^[6-79][0-9]{8}$'


@typechecked
class ContactAttribNotMatch(TypeError):
    def __init__(self, msg):
        self.msg = msg


class ContactFormatException(ValueError):
    def __init__(self, msg):
        self.msg = msg


class ContactNameEmpty(Exception):
    def __init__(self, msg):
        self.msg = msg


class Contact:

    def __init__(self, name: str, tel: str, mail: str, address: str = ""):
        if name == '':
            raise ContactNameEmpty('El nombre no puede estar vacío')
        self.__name = name
        self.tel = tel  # Invoca el Setter de tel
        self.mail = mail
        self.address = address

    @property
    def name(self):
        return self.__name

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, value):
        try:
            if re.match(PATH_NUMBER, value):
                self.__tel = value
            else:
                raise ContactAttribNotMatch('El número de teléfono no coincide.')
        except ContactAttribNotMatch as e:
            print('Error: ' + e.msg)

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, value):
        try:
            if re.match(PATH_MAIL, value):
                self.__mail = value
            else:
                raise ContactAttribNotMatch('El mail no coincide.')
        except ContactAttribNotMatch as e:
            print('Error: ' + e.msg)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def __str__(self):
        return f'Name: {self.__name} ** Tel: {self.__tel} ** Mail: {self.__mail} ** Address: {self.__address}\n'
