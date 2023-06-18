import os.path
import xml.etree.ElementTree as ET
import json

XML_FILE = 'questions.xml'
JSON_FILE = 'questions.json'


def main():
    file = input('Elige entre JSON y XML desea leer: ')

    if not os.path.exists(XML_FILE or JSON_FILE):
        raise FileNotFoundError('El archivo introducido no se ha encontrado.')

    if file == 'XML':

        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        for quest in root.findall('question'):
            for statement in quest.findall('statement'):
                print(f'* {statement.text}: ')
            for option in quest.iter('option'):
                print(f'    - {option.text}')
            print()
            election = input('Elije una opción: ')

            found_option = None
            for option in quest.iter('option'):
                if option.text == election:
                    found_option = option
                    break

            if found_option is None:
                print('Opción inválida. Por favor, elija una opción válida.')
            else:
                print(f'Puntos ganados: {found_option.attrib["points"]}')

    elif file == 'JSON':
        with open(JSON_FILE, encoding='utf-8') as json_file:
            json.load(json_file, object_hook=question_decoder)


def question_decoder(q):
    if 'name' in q and 'statement' in q and 'options' in q and 'base_pointed' in q:
        print('- ' + q['statement'])
        points = 0
        if 'options' in q:
            for option in q['options']:
                print(f'    * ' + str(option[0]))
            election = input('Elije una opción: ')
            for option in q['options']:
                if election == option[0]:
                    points += option[1]
        print(f'La puntuación obtenida es de {points}')
    return q


if __name__ == '__main__':
    main()
