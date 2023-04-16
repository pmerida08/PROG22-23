import json

__BASE_POINTS_MAX = 2
__number_quests = 0

def show():
    count = 0
    with open('questions.json', 'rt', encoding='utf-8') as json_file:
        data = json.load(json_file)

        quest = data[count]
        name = quest['name']
        statement = quest['statement']
        options = quest['options']
        points = quest['base_pointed']

    print(f'{name}{count + 1}: {statement}')


if __name__ == '__main__':
    show()