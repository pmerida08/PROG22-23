from addressbook import AddressBook, AddressFileError, AddressBookContactAlreadyAdded, AddressLimitOfContacts, \
    AddressBookContactNotAdded
from contacts import ContactNameEmpty, ContactAttribNotMatch
import sys

ad_book = AddressBook()


class Menu:

    @staticmethod
    def show_menu():
        print('\nMenu: ')
        print('1. Crear desde fichero xml' + '\n'
        '2. Alta de contacto' + '\n'
        '3. Baja de contacto' + '\n'
        '4. Búsqueda de contacto' + '\n'
        '5. Listado' + '\n'
        '6. Exportar a XML' + '\n'
        '7. Salir del programa.')
        print('-------------------------------------------------------------------------------------------------------'
            '--------')

    @staticmethod
    def choose_option():
        opcion = int(input('Introduce la acción que desee hacer: '))
        match opcion:
            case 1:
                file_to_import = input('Escribe el fichero de donde desea importar: ')
                import_from_xml(file_to_import)
            case 2:
                register_contact()
            case 3:
                to_remove = input('Introduce el nombre del contacto que quieres quitar de la lista: ')
                remove_contact(to_remove)
            case 4:
                to_search = input('Introduce el contacto que quieres buscar: ')
                search_contact(to_search)
            case 5:
                show_list()
            case 6:
                export()
            case 7:
                print('Has salido del programa con éxito.', file=sys.stderr)
                sys.exit(1)
            case _:
                print('La opcion no es correcta')


def remove_contact(name_contact):
    try:
        ad_book.remove_contact(name_contact)
        print('Contacto eliminado con éxito.')
    except AddressBookContactNotAdded:
        print('El contacto que quiere eliminar no existe.')


def search_contact(contact_to_search):
    try:
        found_contact = ad_book.search_contact(contact_to_search)
        print(found_contact)
    except AddressBookContactNotAdded:
        print('El contacto no se ha encontrado.')


def import_from_xml(xml_file: str):
    try:
        ad_book.load_file(xml_file)
        print('Archivo cargado con éxito.')
    except AddressFileError as e:
        print('Error: ' + e.msg)


def register_contact():
    name_contact_to_add = input('Introduce el nombre del contacto que quieres añadir: ')
    tel_contact_to_add = input('Introduce el telefono del contacto que quieres añadir: ')
    mail_contact_to_add = input('Introduce el correo del contacto que quieres añadir: ')
    address_contact_to_add = input('Introduce la dirección del contacto que quieres añadir: ')
    try:
        ad_book.register_contact(name_contact_to_add, tel_contact_to_add, mail_contact_to_add, address_contact_to_add)
        print('Contacto añadido con éxito.')
    except AddressBookContactAlreadyAdded as e:
        print('Error: ' + e.msg)
    except AddressLimitOfContacts as e:
        print('Error: ' + e.msg)
    except ContactNameEmpty as e:
        print('Error: ' + e.msg)
    except ContactAttribNotMatch as e:
        print('Error: ' + e.msg)


def show_list():
    print(ad_book.show_addressbook())


def export():
    try:
        xml_file = input('Indica en qué archivo xml exportar los contactos: ')
        ad_book.export_to_xml(xml_file)
    except AddressFileError as e:
        print('Error: ' + e.msg)


if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.show_menu()
        menu.choose_option()
