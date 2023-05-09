import xml.etree.ElementTree as ET

XML_FILE = 'questions.xml'

tree = ET.parse(XML_FILE)
root = tree.getroot()


def show():
    for quest in root.findall('question'):
        for statement in quest.findall('statement'):
            print(f'* {statement.text}: ')
        for option in quest.iter('option'):
            print(f'    - {option.text}')
        print()
        election = choose_option()
        check(election)


def choose_option():
    option = input('Elije una opción: ')
    return option


def check(opt_chosen):
    for option in root.findall('options'):
        if option == opt_chosen:
            return f'{option.attrib["points"]}'


if __name__ == '__main__':
    show()
