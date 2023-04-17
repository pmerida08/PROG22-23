from question_v1 import Question

q1 = Question('q1', '¿Qué son los mamíferos?',
[('Seres vivos', 2), ('Plantas', -0.25), ('Insectos', -0.25), ('Partido político', -0.25)], 1)
q1.show()
q1.answer()

q2 = Question('q2', '¿En qué meridiano está España?',
[('M. magnético', -0.25), ('M. de Greenwich', 2), ('M. cero', -0.25), ('Ecuador', -0.25)], 1)
q2.show()
q2.answer()

q3 = Question('q3', '¿Cuál es la capital de Marruecos?',
[('Ceuta', -0.25), ('Melilla', -0.25), ('Rabat', 2), ('Marrakech', -0.25)], 1)
q3.show()
q3.answer()

q4 = Question('q4', '¿En qué año murió Francisco Franco?',
[('1976', -0.25), ('1973', -0.25), ('1978', -0.25), ('1975', 2)], 1)
q4.show()
q4.answer()

q5 = Question('q5', '¿Cuál fue el primer programador/a?',
[('Ada Lovelace', 2), ('von Neumann', -0.25), ('Peter Griffin', -0.25), ('Bill Gates', -0.25)], 1)
q5.show()
q5.answer()

