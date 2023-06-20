import json
from question import QuestionError, Question

JSON_FILE = "questions.json"

with open(JSON_FILE, 'rt', encoding='utf-8') as file:
    data = json.load(file)

    total_points = 0

    for question in data:
        options = question['options']
        question['options'] = [(str(option), float(score)) for option, score in options]

        name = (question['name'])
        statement = (question['statement'])
        options = (question['options'])
        points = (question['base_pointed'])

        q = Question(name, statement, options, points)
        print(q.name + f'. {q.enunciate}')
        for e in q.elections:
            print(f'- {e[0]}')

        try:
            answer = int(input('\n¿Cuál es la respuesta correcta?: '))
            print(f'Puntuación obtenida: {q.get_points(answer)} puntos.\n')
            total_points += q.get_points(answer)
        except ValueError:
            print('La respuesta debe ser un entero.\n')
        except QuestionError as e:
            print(f'\n{e}')

    print(f'Puntuación total de {total_points / len(data) * 10} puntos. ')
