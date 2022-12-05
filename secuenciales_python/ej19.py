"""
Escribir un programa para calcular la nota final de un estudiante, considerando que:

    - cada respuesta correcta suma 5 puntos
    - cada respuesta incorrecta suma -1 puntos
    - cada respuesta en blanco suma 0 puntos.
"""
MAX_SCORE = 10
POINTS_INCORRECT_ANSWERS = -1
POINTS_CORRECT_ANSWERS = 5

correcta = int(input('Introduce las respuestas correctas: '))
falladas = int(input('Introduce las respuestas falladas: '))
vacias = int(input('Introduce las respuestas vacías: '))

suma = correcta + falladas + vacias
max_total = suma * POINTS_CORRECT_ANSWERS
puntuacion = correcta * POINTS_CORRECT_ANSWERS + falladas * POINTS_INCORRECT_ANSWERS

calificacion = (puntuacion/max_total) * MAX_SCORE

print('La puntuación del estudiante es de: ', calificacion)
