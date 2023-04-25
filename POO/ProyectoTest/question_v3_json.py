import json
from dataclasses import dataclass
from json import JSONEncoder
from typeguard import typechecked

JSON_FILE = "questions.json"

@typechecked
@dataclass(frozen=True)
class Question:
    name: str
    statement: str
    options: list[tuple[str, float]]
    base_pointed: int

class QuestionEncoder(JSONEncoder):
    def default(self, dec):
        return dec.__dict__

if __name__ == '__main__':
    questions = [
        Question('q1', '¿Qué son los mamíferos?',[('Seres vivos', 2), ('Plantas', -0.25), ('Insectos', -0.25), ('Partido político', -0.25)], 1),
        Question('q2', '¿En qué meridiano está España?',[('M. magnético', -0.25), ('M. de Greenwich', 2), ('M. cero', -0.25), ('Ecuador', -0.25)], 1),
        Question('q3', '¿Cuál es la capital de Marruecos?',[('Ceuta', -0.25), ('Melilla', -0.25), ('Rabat', 2), ('Marrakech', -0.25)], 1),
        Question('q4', '¿En qué año murió Francisco Franco?',[('1976', -0.25), ('1973', -0.25), ('1978', -0.25), ('1975', 2)], 1),
        Question('q5', '¿Cuál fue el primer programador/a?',[('Ada Lovelace', 2), ('von Neumann', -0.25), ('Peter Griffin', -0.25), ('Bill Gates', -0.25)], 1)
    ]

    with open(JSON_FILE, "wt", encoding='utf-8') as file:
        json.dump(questions, file, ensure_ascii=False, indent=4, cls=QuestionEncoder)

    print(f'Creado {JSON_FILE}')