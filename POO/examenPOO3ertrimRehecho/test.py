from addressbook import AddressBook, AddressBookError
from contact import ContactError
from menu import Menu

ad_book = AddressBook()


def main():
    m = Menu('Crear desde fichero xml', 'Alta de contacto', 'Baja de contacto', 'Búsqueda de contacto',
                'Listado', 'Exportar a XML', 'Salir del programa', title='Gestión de Agenda de Contactos')
    while True:
        opcion = m.choose()
        match opcion:
            case 1: import_from_xml()
            case 2: register_contact()
            case 3: remove_contact()
            case 4: search_contact()
            case 5: show_list()
            case 6: export_to_xml()
            case 7: break


def remove_contact():
    try:
        name_contact = input('Introduce el contacto a eliminar: ')
        ad_book.remove_contact(name_contact)
        print('Contacto eliminado con éxito.')
    except AddressBookError as e:
        print(f'\nERROR: {e}\n')


def search_contact():
    try:
        contact_to_search = input('Introduce el contacto que quieres buscar: ')
        found_contact = ad_book.search_contact(contact_to_search)
        print(found_contact)
    except AddressBookError as e:
        print(f'\nERROR: {e}\n')


def import_from_xml():
    global ad_book
    xml_file = input('Introduce el archivo XML que desea importar: ')
    try:
        ad_book = AddressBook(xml_file)
        print('Archivo cargado con éxito.')
    except AddressBookError as e:
        print(f'\nERROR: {e}\n')


def register_contact():
    name_contact_to_add = input('Introduce el nombre del contacto que quieres añadir: ')
    tel_contact_to_add = input('Introduce el telefono del contacto que quieres añadir: ')
    mail_contact_to_add = input('Introduce el correo del contacto que quieres añadir: ')
    address_contact_to_add = input('Introduce la dirección del contacto que quieres añadir: ')
    try:
        ad_book.register_contact(name_contact_to_add, tel_contact_to_add, mail_contact_to_add, address_contact_to_add)
        print('\nContacto añadido con éxito.\n')
    except AddressBookError as e:
        print(f'\nERROR: {e}\n')
    except ContactError as e:
        print(f'\nERROR: {e}\n')


def show_list():
    print(ad_book)


def export_to_xml():
    try:
        xml_file = input('Indica en qué archivo xml exportar los contactos: ')
        ad_book.export_to_xml(xml_file)
        print('\nLista de contactos añadida correctamente.\n')
    except AddressBookError as e:
        print(f'\nERROR: {e}\n')


if __name__ == '__main__':
    main()
