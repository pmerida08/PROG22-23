import xml.etree.ElementTree as ET
from xml.dom import minidom
from typeguard import typechecked
from contact import Contact

PATTERN_XML = r'\w+\.xml'


@typechecked
class AddressBookError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class AddressLimitOfContacts(AddressBookError):
    def __init__(self, msg):
        super().__init__(msg)


class AddressBookFormatFileError(AddressBookError):
    def __init__(self, msg):
        super().__init__(msg)


class AddressBookContactAlreadyAddedError(AddressBookError):
    def __init__(self, msg):
        super().__init__(msg)


class AddressBookContactNotAddedError(AddressBookError):
    def __init__(self, msg):
        super().__init__(msg)


class AddressBookFileError(AddressBookError):
    def __init__(self, msg):
        super().__init__(msg)


class AddressBook:
    __CONTACTS_LIMIT = 100

    def __init__(self, xml_file: str = None):
        self.__listed_contacts = []

        if xml_file:
            self.__load_file(xml_file)

    def __load_file(self, xml_file: str):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for contact in range(root):
                name = root[contact][0].text
                tel = root[contact][1].text
                mail = root[contact][2].text
                address = root[contact][3].text
                self.register_contact(name, tel, mail, address)
        except OSError as e:
            raise AddressBookFileError(f'Hay problemas para poder abrir el archivo. ERROR: {e}')

    def register_contact(self, name: str, tel: str, mail: str, address: str = None):
        if len(self.__listed_contacts) >= AddressBook.__CONTACTS_LIMIT:
            raise AddressLimitOfContacts(f'El límite de contactos es de {AddressBook.__CONTACTS_LIMIT}')
        if self.search_contact(name):
            raise AddressBookContactAlreadyAddedError('El contacto ya ha sido añadido.')
        contact = Contact(name, tel, mail, address)
        self.__listed_contacts.append(contact)

    def search_contact(self, name: str):
        for contact in self.__listed_contacts:
            if contact.name == name:
                return contact

    def remove_contact(self, name: str):
        to_remove = self.search_contact(name)
        if to_remove is None:
            raise AddressBookContactNotAddedError('El contacto que intenta eliminar no existe')
        self.__listed_contacts.remove(to_remove)

    def __str__(self):
        contact_str = ''
        for contact in self.__listed_contacts:
            contact_str += str(contact)
        return f'{contact_str}'

    def export_to_xml(self, xml_file: str):
        try:
            root = ET.Element('addressbook')

            for c in self.__listed_contacts:
                contact = ET.SubElement(root, 'contact')
                ET.SubElement(contact, 'name').text = c.name
                ET.SubElement(contact, 'tel').text = c.tel
                ET.SubElement(contact, 'mail').text = c.mail
                ET.SubElement(contact, 'address').text = c.address

            tree = ET.ElementTree(root)
            tree.write(xml_file, encoding='unicode')

            xml_str = minidom.parseString(ET.tostring(root)).toprettyxml()

            with open(xml_file, "w") as f:  # TODO Ser un vago redomado (no hace falta abrirlo).
                f.write(xml_str)
        except OSError as e:
            raise AddressBookError(f'Error: Ha habido problemas para abrir el archivo. {e}')
