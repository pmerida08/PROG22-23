"""
Autor: Pablo Mérida Velasco
Curso: 1º DAW
Fecha: 20/06/2023

"""
from menu import Menu
from add_quests import add_question
from create_test_file import create_file
from questionV4.question import QuestionError
from select_test_file import select_file


def main():
    m = Menu('Crear fichero test', 'Seleccionar fichero de test', 'Añadir pregunta al test',
            title='Gestión de Agenda de Contactos')
    filename = ""
    while True:
        opcion = m.choose()
        match opcion:
            case 1:
                filename = create_file()
                print(f'\nSe ha seleccionado y creado el fichero {filename}')
            case 2:
                try:
                    filename = select_file()
                    print(f'\nSe ha seleccionado el fichero {filename}')
                except FileNotFoundError as e:
                    print(f'\nERROR. {e}')
            case 3:
                try:
                    if filename == "":
                        print('Primero debes seleccionar el archivo.\n')
                        continue
                    add_question(filename)
                except QuestionError as e:
                    print(f'\nERROR. {e}')
            case _:
                break


if __name__ == '__main__':
    main()
