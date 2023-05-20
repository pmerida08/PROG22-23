import xml.etree.ElementTree as ET
import json
import re

XML_FILE = 'questions.xml'
JSON_FILE = 'questions.json'
path_xml = r'\w+\.xml'
path_json = r'\w+\.json'


def main():
    file = input('Escribe el archivo que se desea leer: ')

    if re.match(path_xml, file):

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

    elif re.match(path_json, file):
        with open(JSON_FILE, encoding='utf-8') as json_file:
            questions = json.load(json_file, object_hook=question_decoder)

        print(questions)
    else:
        raise FileNotFoundError('El archivo introducido no se ha encontrado.')


def question_decoder(q):
    if 'name' in q and 'statement' in q and 'options' in q and 'base_pointed' in q:
        print('- ' + q['statement'])
        if 'options' in q:
            for option in q['options']:
                print(f'    * ' + str(option[0]))
    return q


if __name__ == '__main__':
    main()
