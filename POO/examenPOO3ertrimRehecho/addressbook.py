import os.path
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from typeguard import typechecked
from contacts import Contact

PATH_XML = r'\w+\.xml'


@typechecked
class AddressLimitOfContacts(Exception):
    def __init__(self, msg):
        self.msg = msg


class AddressFileError(Exception):
    def __init__(self, msg):
        self.msg = msg


class AddressBookContactAlreadyAdded(Exception):
    def __init__(self, msg):
        self.msg = msg


class AddressBookContactNotAdded(Exception):
    def __init__(self, msg):
        self.msg = msg


class AddressBook:
    __CONTACTS_LIMIT = 5

    def __init__(self, xml_file: str = None):
        self.__listed_contacts = set()

        if xml_file and re.match(PATH_XML, xml_file):
            self.load_file(xml_file)

    def load_file(self, xml_file):
        if os.path.exists(f'./{xml_file}'):
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for contact in root.findall('contact'):
                name = contact.find('name').text
                tel = contact.find('tel').text
                mail = contact.find('mail').text
                address = contact.find('address').text

                self.__listed_contacts.add(Contact(name, tel, mail, address))
        raise AddressFileError('Hay problemas para poder escribir en el archivo.')

    def show_addressbook(self):
        contact = ''
        for c in self.__listed_contacts:
            contact += str(c)
        return contact

    def register_contact(self, name: str, tel: str, mail: str, address: str = None):
        if len(self.__listed_contacts) > AddressBook.__CONTACTS_LIMIT:
            raise AddressLimitOfContacts(f'El límite de contactos es de {AddressBook.__CONTACTS_LIMIT}')
        if self.search_contact(name):
            raise AddressBookContactAlreadyAdded('El contacto ya ha sido añadido.')
        contact = Contact(name, tel, mail, address)
        self.__listed_contacts.add(contact)

    def search_contact(self, name: str):
        for contact in self.__listed_contacts:
            if contact.name == name:
                return contact

    def remove_contact(self, name: str):
        to_remove = self.search_contact(name)
        if to_remove is None:
            raise AddressBookContactNotAdded('El contacto que intenta eliminar no existe')
        self.__listed_contacts.remove(to_remove)

    def export_to_xml(self, xml_file: str):
        if os.path.exists(f'./{xml_file}'):
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
        raise AddressFileError('Hay problemas para poder escribir en el archivo.')
