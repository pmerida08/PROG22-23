from question import Question, QuestionError

questions = [
    Question('Question 1', '¿Qué son los mamíferos?',
             [('Seres vivos', 1), ('Plantas', -0.25), ('Insectos', -0.25), ('Partido político', -0.25)], 1),
    Question('Question 2', '¿En qué meridiano está España?',
             [('M. magnético', -0.25), ('M. de Greenwich', 1), ('M. cero', -0.25), ('Ecuador', -0.25)], 1),
    Question('Question 3', '¿Cuál es la capital de Marruecos?',
             [('Ceuta', -0.25), ('Melilla', -0.25), ('Rabat', 1), ('Marrakech', -0.25)], 1),
    Question('Question 4', '¿En qué año murió Francisco Franco?',
             [('1976', -0.25), ('1973', -0.25), ('1978', -0.25), ('1975', 1)], 1),
    Question('Question 5', '¿Cuál fue el primer programador/a?',
             [('Ada Lovelace', 1), ('von Neumann', -0.25), ('Peter Griffin', -0.25), ('Bill Gates', -0.25)], 1)
]

total_points = 0

for q in questions:
    print(q.name + f'. {q.enunciate}')
    for e in q.elections:
        print(f'- {e[0]}')

    try:
        answer = int(input('\n¿Cuál es la respuesta correcta?: '))
        question_score = q.get_points(answer)
        if answer == 0:
            question_score = 0
        print(f'Puntuación obtenida: {question_score} puntos.\n')
        total_points += question_score
    except ValueError:
        print('\nLa respuesta debe ser un entero.')
    except QuestionError as e:
        print(f'\n{e}')

print(f'Puntuación total de {(total_points / len(questions)) * 10}/10 ')
