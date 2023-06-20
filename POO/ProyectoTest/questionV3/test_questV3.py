import xml.etree.ElementTree as ET
from question import QuestionError, Question

XML_FILE = 'questions.xml'

total_points = 0
tree = ET.parse(XML_FILE)
root = tree.getroot()

for i in range(len(root)):
    name = root[i].get('name')
    base_score = root[i].get('base_score')
    statement = root[i][0].text.strip()
    options = root[i][1]
    options_list = []
    for j in range(len(options)):
        option = root[i][1][j].text.strip()
        points = root[i][1][j].get('points')
        options_list.append((option, float(points)))

    question = Question(name, statement, options_list, int(base_score))

    print(question.name + f'. {question.enunciate}')
    for e in question.elections:
        print(f'- {e[0]}')
    try:
        answer = int(input('\n¿Cuál es la respuesta correcta?: '))
        print(f'Puntuación obtenida: {question.get_points(answer)} puntos.\n')
        total_points += question.get_points(answer)
    except ValueError:
        print('La respuesta debe ser un entero.\n')
    except QuestionError as e:
        print(f'\n{e}')

print(f'Puntuación total de {total_points / len(root) * 10} puntos. ')
