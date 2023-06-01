import sys

from POO.examenPOO3ertrimRehecho.addressbook import ContactFormatException
from addressbook import AddressBook


while True:
    print('\nMenu: ')
    print('1. Crear desde fichero xml' + '\n'
            '2. Alta de contacto' + '\n'
            '3. Baja de contacto' + '\n'
            '4. Búsqueda de contacto' + '\n'
            '5. Listado' + '\n'
            '6. Exportar a XML' + '\n'
            '7. Salir del programa.')
    print('-------------------------------------------------------------------------------------------------------'
        '--------' + '\n')

    addressbook = AddressBook()

    opcion = int(input('Introduce la acción que desee hacer: '))
    match opcion:
        case 1:
            addressbook1 = AddressBook('addressbook.xml')
        case 2:
            name_contact_to_add = input('Introduce el nombre del contacto que quieres añadir: ')
            tel_contact_to_add = input('Introduce el telefono del contacto que quieres añadir: ')
            mail_contact_to_add = input('Introduce el correo del contacto que quieres añadir: ')
            address_contact_to_add = input('Introduce la dirección del contacto que quieres añadir: ')
            try:
                addressbook.register_contact(name_contact_to_add, tel_contact_to_add, mail_contact_to_add,
                                        address_contact_to_add)
            except ContactFormatException:
                print('El formato de alguno/s de los parámetros no son los adecuados.')
                continue
        case 3:
            contact_to_remove = input('Introduce el contacto que quieres quitar: ')
            addressbook.remove_contact(contact_to_remove)

        case 4:
            contact_to_search = input('Introduce el contacto para buscar: ')
            print(addressbook.search_contact(contact_to_search))

        case 5:
            addressbook.show_addressbook()

        case 6:
            input('¿En qué archivo quieres exportar la lista de contactos?')
            addressbook.export_to_xml('addressbook.xml')

        case 7:
            print('Has salido del programa con éxito.', file=sys.stderr)
            sys.exit(1)
        case _:
            print('La opcion no es correcta')
            break
