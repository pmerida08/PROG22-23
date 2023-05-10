import xml.etree.ElementTree as ET

XML_FILE = 'questions.xml'

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
