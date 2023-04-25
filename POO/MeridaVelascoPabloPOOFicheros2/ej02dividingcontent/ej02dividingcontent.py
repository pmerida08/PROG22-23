"""
2. Escribe un programa que guarde en un fichero el contenido de otros dos ficheros, de tal forma que en el fichero
resultante aparezcan las líneas de los primeros dos ficheros mezcladas, es decir, la primera línea será del primer
fichero, la segunda será del segundo fichero, la tercera será la siguiente del primer fichero, etc.

Los nombres de los dos ficheros origen y el nombre del fichero destino se deben pasar como argumentos en la línea de
comandos.

Hay que tener en cuenta que los ficheros de donde se van cogiendo las líneas pueden tener tamaños diferentes.

"""
LINES = 11
wrapped_lines = []

for i in range(1, LINES):
    if i % 2 == 0:
        with open('file2.txt', 'r+t', encoding='utf-8') as file:
            file.seek(0,2)
            str_ = f'Esta es la línea {i}\n'
            file.write(str_)
            wrapped_lines.append(str_)
    else:
        with open('file1.txt', 'r+t', encoding='utf-8') as file:
            file.seek(0, 2)
            str_ = f'Esta es la línea {i}\n'
            file.write(str_)
            wrapped_lines.append(str_)

with open('finaltext.txt', 'r+t', encoding='utf-8') as file:
    file.writelines(wrapped_lines)
