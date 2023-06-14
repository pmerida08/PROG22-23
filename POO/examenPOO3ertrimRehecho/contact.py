import re
from typeguard import typechecked

"""
Contacto que se añade
"""


@typechecked
class ContactError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ContactNameEmptyError(ContactError):
    def __init__(self, msg):
        super().__init__(msg)


class ContactMailNotMatchError(ContactError):
    def __init__(self, msg):
        super().__init__(msg)


class ContactTelNotMatchError(ContactError):
    def __init__(self, msg):
        super().__init__(msg)


class Contact:
    __PATTERN_MAIL = re.compile(r'[^@\t\r\n]+@[^@\t\r\n]+\.[^@\t\r\n]+')
    __PATTERN_PHONE = re.compile(r'[679][0-9]{8}')

    def __init__(self, name: str, tel: str, mail: str, address: str = ""):
        if name == '':
            raise ContactNameEmptyError('El nombre no puede estar vacío')
        self.__name = name
        self.tel = tel
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
        if not Contact.__PATTERN_PHONE.fullmatch(value):
            raise ContactTelNotMatchError('El número de teléfono no coincide.')
        self.__tel = value

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, value):
        if not Contact.__PATTERN_MAIL.fullmatch(value):
            raise ContactMailNotMatchError('El mail no coincide.')
        self.__mail = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def __str__(self):
        return f'Name: {self.__name} ** Tel: {self.__tel} ** Mail: {self.__mail} ** Address: {self.__address}\n'
