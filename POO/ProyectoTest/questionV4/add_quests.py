"""
3. Añadir pregunta al test.

- Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.

- Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.

- Comprobamos que los datos son correctos, para ello podríamos crear un objeto Question y si no lanza excepción es que
están bien.

- Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).

- Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el
fichero.
"""
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from question import Question, QuestionValueError
from typeguard import typechecked

MAX_OPTIONS = 4


@typechecked
def validate_question(name, enunciate, options, base_pointed):
    question = Question(name, enunciate, options, base_pointed)
    if not question.name:
        raise QuestionValueError(question.name)
    if not question.enunciate:
        raise QuestionValueError(question.enunciate)
    if not question.elections:
        raise ValueError(question.elections)
    if not question.base_pointed:
        raise ValueError(question.base_pointed)


def add_question(filename: str):
    if filename[-4:] == '.xml':
        tree = ET.parse(filename)
        root = tree.getroot()

        name = input('Introduce el nombre de la pregunta: ')
        enunciate = input('Introduce el enunciado de la pregunta: ')
        base_pointed = input('Introduce la puntuación base de la pregunta: ')

        question = ET.Element('question', {'name': name, 'base_pointed': base_pointed})
        statement = ET.SubElement(question, 'statement')
        statement.text = enunciate
        options = ET.SubElement(question, 'options')

        for i in range(MAX_OPTIONS):
            option = input(f"Escribe la opción {i + 1}: ")
            points = input(f"Escribe el valor de la opción {i + 1}: ")
            posible_option = ET.SubElement(options, 'option', {'points': points})
            posible_option.text = option

        validate_question(name, statement, options, base_pointed)

        root.append(question)

        tree.write(filename, encoding='utf-8', xml_declaration=True)

        # Para poner el archivo 'xml' bonito
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml()

        with open(filename, 'w') as file:
            file.write(xml_str)

    elif filename[-5:] == '.json':

        question_title = input("Introduce el titulo de la pregunta: ")
        base_score = int(input("Introduce la puntuación de la pregunta: "))
        question_statement = input("Introduce el enunciado de la pregunta: ")

        question_data = {
            'name': question_title,
            'base_score': base_score,
            'statement': question_statement,
            'options': []
        }
        for i in range(MAX_OPTIONS):
            option = input(f"Escribe la opción {i + 1}: ")
            weight = input(f"Escribe el valor de la opción {i + 1}: ")
            option_data = {
                'option': option,
                'weight': weight
            }
            question_data['options'].append(option_data)

        with open(filename, 'r') as f:
            try:
                questions = json.load(f)
            except ValueError:
                questions = []

        questions.append(question_data)

        with open(filename, 'w') as f:
            json.dump(questions, f, indent=2)
