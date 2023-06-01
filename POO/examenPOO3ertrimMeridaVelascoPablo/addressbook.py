import re
from typeguard import typechecked
import xml.etree.ElementTree as ET
from xml.dom import minidom

CONTACTS_LIMIT = 5

PATH_MAIL = r'[^@\t\r\n]+@[^@\t\r\n]+\.[^@\t\r\n]+'

PATH_NUMBER = r'^[6-79][0-9]{8}$'

PATH_XML = r'\w+\.xml'


@typechecked
class Contact:

    def __init__(self, name: str, tel: str, mail: str, address: str = None):
        if name == '':
            raise ValueError('El nombre no puede estar vacío')
        self.__name = name

        if re.match(PATH_NUMBER, tel):
            self.__tel = tel
        else:
            raise ValueError('El numero de telefono no coincide.')

        if re.match(PATH_MAIL, mail):
            self.__mail = mail
        else:
            raise ValueError('El mail no coincide.')

        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, value):
        self.__tel = value

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, value):
        self.__mail = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def __str__(self):
        return f'Name: {self.__name} ** Tel: {self.__tel} ** Mail: {self.__mail} ** Address: {self.__address}\n'


class AddressLimitOfContacts(Exception):
    def __init__(self, msg):
        self.__msg = msg


class ContactAlreadyAdded(Exception):
    def __init__(self, msg):
        self.__msg = msg


class ContactNotFound(Exception):
    def __init__(self, msg):
        self.__msg = msg


class AddressBook:

    def __init__(self, xml_file: str = None):
        if xml_file and re.match(PATH_XML, xml_file):
            self.__xml_file = xml_file
        self.__listed_contacts = []

    def search_contact(self, name: str):
        for contact in self.__listed_contacts:
            if contact.name == name:
                return contact

    def remove_contact(self, name: str):
        to_remove = self.search_contact(name)
        self.__listed_contacts.remove(to_remove)

    def register_contact(self, name: str, tel: str, mail: str, address: str = None):
        if len(self.__listed_contacts) > CONTACTS_LIMIT:
            raise AddressLimitOfContacts('El límite de contactos es de 5')
        if self.search_contact(name):
            raise ContactAlreadyAdded('El contacto ya ha sido añadido.')
        contact = Contact(name, tel, mail, address)
        self.__listed_contacts.append(contact)

    def show_addressbook(self):
        for contact in self.__listed_contacts:
            return contact

    def export_to_xml(self, xml_file: str):
        if re.match(PATH_XML, xml_file):
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for c in self.__listed_contacts:
                contact = ET.SubElement(root, 'contact')
                name = ET.SubElement(contact, 'name')
                name.text = c.name
                tel = ET.SubElement(contact, 'tel')
                tel.text = c.tel
                mail = ET.SubElement(contact, 'mail')
                mail.text = c.mail
                address = ET.SubElement(contact, 'address')
                address.text = c.address

            tree = ET.ElementTree(root)
            tree.write(xml_file, encoding='unicode')

            xml_str = minidom.parseString(ET.tostring(root)).toprettyxml()

            with open(xml_file, "w") as f:
                f.write(xml_str)
            print('Importado con éxito.')
        else:
            raise ValueError('El formato del archivo xml no es válido.')
