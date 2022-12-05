"""
Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de PROGRAMACIÓN,
LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMATICOS.

El número de alumnos no lo sabemos de antemano por lo que se han de añadir conforme se vayan introduciendo los datos.

El programa pedirá el nombre y apellidos del alumno y a continuación las calificaciones en los módulos mencionados
anteriormente.

Cuando el usuario desee dejar de introducir información deberá de introducir una cadena vacía al introducir el nombre.

Asimismo el programa deberá de proporcionar las siguientes funcionalidades:

    Impresión de las calificaciones del curso completo.

    Impresión de las calificaciones de un alumno en concreto. El programa pedirá nombre y apellidos del alumno y de
    encontrarlo mostrará las calificaciones de todos los módulos de este alumno.

    Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota media.

    Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota máxima
    así como el alumno con la misma.

    Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota más
    baja así como el alumno con la misma.

    Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá de
    ser capaz de realizar una ordenación descendente por dicha nota.

Este programa es mejor hacerlo con funciones, saldrá más corto, más legible y más eficiente.

Nota: En las listas de python se pueden mezclar datos de diferente tipo. Aprovecha los módulos y funciones de python que
faciliten las operaciones que se piden.

Autor: Pablo Mérida Velasco
Fecha: 28/11/2022
"""
import sys


def input_marks():
    while True:
        student_name = input('\nDame el nombre y apellidos del alumno/a: ')
        if student_name == '':
            break
        mark1 = float(input('Dame su nota de PROGRAMACION: '))
        mark2 = float(input('Dame su nota de LENGUAJE DE MARCAS: '))
        mark3 = float(input('Dame su nota de BASE DE DATOS: '))
        mark4 = float(input('Dame su nota de SISTEMAS INF.: '))
        students.append([student_name, mark1, mark2, mark3, mark4])


def print_marks_course():
    print(students)


def print_marks_student():
    while True:
        name = input('\nIntroduce el nombre y el apellido del alumno del que se quiere saber la nota: ')

        for i in range(len(students)):
            if students[i][0] == name:
                print(f'Las notas del alumno {name} son: \n'
                      f'PROGRAMACION: {students[i][1]}, \n'
                      f'LENGUAJE DE MARCAS: {students[i][2]}, \n'
                      f'BASE DE DATOS: {students[i][3]}, \n'
                      f'SISTEMAS INFORMÁTICOS: {students[i][4]}')
            else:
                continue


def print_mean_module():

    module = input('\nIntroduce el módulo del cual se desea mostrar la media: ')
    match module:
        case 'PROGRAMACIÓN':
            summary = 0
            for i in range(len(students)):
                summary += students[i][1]
            mean = summary / len(students)
            print(f'La media de las notas de la asignatura {module} es de: {mean}')
        case 'LENGUAJE DE MARCAS':
            summary = 0
            for i in range(len(students)):
                summary += students[i][2]
            mean = summary / len(students)
            print(f'La media de las notas de la asignatura {module} es de: {mean}')
        case 'BASE DE DATOS':
            summary = 0
            for i in range(len(students)):
                summary += students[i][3]
            mean = summary / len(students)
            print(f'La media de las notas de la asignatura {module} es de: {mean}')
        case 'SISTEMAS INFORMÁTICOS':
            summary = 0
            for i in range(len(students)):
                summary += students[i][4]
            mean = summary / len(students)
            print(f'La media de las notas de la asignatura {module} es de: {mean}')


def print_max_mark_module():

    module = input('\nIntroduce el módulo del cual se desea mostrar la nota máxima: ')
    match module:
        case 'PROGRAMACIÓN':
            maximum = 0
            for i in range(len(students)):
                if maximum > float(students[i][1]):
                    maximum = students
            print(f'La nota máxima de la asignatura {module} es de: {maximum}')
        case 'LENGUAJE DE MARCAS':
            maximum = 0
            for i in range(len(students)):
                if maximum > float(students[i][2]):
                    maximum = students
            print(f'La nota máxima de la asignatura {module} es de: {maximum}')
        case 'BASE DE DATOS':
            maximum = 0
            for i in range(len(students)):
                if maximum > float(students[i][3]):
                    maximum = students
            print(f'La nota máxima de la asignatura {module} es de: {maximum}')
        case 'SISTEMAS INFORMÁTICOS':
            maximum = 0
            for i in range(len(students)):
                if maximum > float(students[i][4]):
                    maximum = students
            print(f'La nota máxima de la asignatura {module} es de: {maximum}')


def print_min_mark_module():

    module = input('\nIntroduce el módulo del cual se desea mostrar la nota mínima: ')
    match module:
        case 'PROGRAMACIÓN':
            minimum = 0
            for i in range(len(students)):
                if minimum < students[i][1]:
                    minimum = students
            print(f'La nota mínima de la asignatura {module} es de: {minimum}')
        case 'LENGUAJES DE MARCAS':
            minimum = 0
            for i in range(len(students)):
                if minimum < students[i][2]:
                    minimum = students
            print(f'La nota mínima de la asignatura {module} es de: {minimum}')
        case 'BASES DE DATOS':
            minimum = 0
            for i in range(len(students)):
                if minimum < students[i][3]:
                    minimum = students
            print(f'La nota mínima de la asignatura {module} es de: {minimum}')
        case 'SISTEMAS INFORMÁTICOS':
            minimum = 0
            for i in range(len(students)):
                print(students[i][4])
                if minimum < students[i][4]:
                    minimum = students
            print(f'La nota mínima de la asignatura {module} es de: {minimum}')


def print_students_sorted():

    module = input('\nIntroduce el módulo del cual se desea mostrar las notas de mayor a menor: ')
    match module:
        case 'PROGRAMACIÓN':
            array_marks = []
            array_sorted = []
            for i in range(len(students)):
                array_marks.append(students[i][1])
            array_marks.sort(reverse=True)

            for i in range(len(students)):
                for j in range(len(students)):
                    if array_marks[i] == students[j]:
                        array_sorted.append(students[j])
            print(array_sorted)
        case 'LENGUAJES DE MARCAS':
            array_marks = []
            array_sorted = []
            for i in range(len(students)):
                array_marks.append(students[i][3])
            array_marks.sort(reverse=True)

            for i in range(len(students)):
                for j in range(len(students)):
                    if array_marks[i] == students[j]:
                        array_sorted.append(students[j])
            print(array_sorted)
        case 'BASES DE DATOS':
            array_marks = []
            array_sorted = []
            for i in range(len(students)):
                array_marks.append(students[i][3])
            array_marks.sort(reverse=True)

            for i in range(len(students)):
                for j in range(len(students)):
                    if array_marks[i] == students[j]:
                        array_sorted.append(students[j])
            print(array_sorted)
        case 'SISTEMAS INFORMÁTICOS':
            array_marks = []
            array_sorted = []
            for i in range(len(students)):
                array_marks.append(students[i][4])
            array_marks.sort(reverse=True)

            for i in range(len(students)):
                for j in range(len(students)):
                    if array_marks[i] == students[j]:
                        array_sorted.append(students[j])


def exit_code():
    print('Has salido del progranma con éxito. ', file=sys.stderr)
    sys.exit(1)


print('Gestión de Notas')
print('----------------')

# Pedimos las notas del alumnado
students = []
input_marks()

# TODO: ciclo donde pedimos los datos de cada alumno y lo metemos en la lista

# Menu de opciones
while True:
    # mostramos las opciones del menú
    print(
        """
    Menú de opciones para gestionar notas:
    ------------------------------------------------------------------------
    1.  Impresión de las calificaciones del curso completo.
    2.  Impresión de las calificaciones de un alumno en concreto. El programa pedirá nombre y apellidos del alumno y de
        encontrarlo mostrará las calificaciones de todos los módulos de este alumno.
    3.  Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota 
    media. 
    4.  Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota 
    máxima así como el alumno con la misma. 
    5.  Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la 
    nota más baja así como el alumno con la misma. 
    6.  Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá 
    de ser capaz de realizar una ordenación descendente por dicha nota.
    7.  Finalizar.
        """
    )
    opcion = int(input('Introduzca una opción: '))
    match opcion:
        case 1:
            print_marks_course()
        case 2:
            print_marks_student()
        case 3:
            print_mean_module()
        case 4:
            print_max_mark_module()
        case 5:
            print_min_mark_module()
        case 6:
            print_students_sorted()
        case 7:
            exit_code()
        case _:
            print('La opcion no es correcta')
            break
