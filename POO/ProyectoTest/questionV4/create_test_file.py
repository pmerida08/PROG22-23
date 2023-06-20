"""
1. Crear fichero de test.

- Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.

- La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
    programa únicamente maneja estos dos formatos.

- Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.

- Finalmente, se creará el fichero correspondiente.

"""

import os.path
import xml.etree.ElementTree as ET


def ask_file():
    filename = input('Introduce el nombre del archivo con extensión XML o JSON: ')
    extension = filename[-5:]
    return filename, extension


def check_if_file_exists(filename):
    if os.path.exists(filename):
        return True
    return False


def create_file():
    filename, extension = ask_file()

    while True:
        if extension == '.json':
            if not check_if_file_exists(filename):
                f = open(filename, 'wt', encoding='utf-8')
                f.close()
                print(f'El fichero {filename} se ha creado correctamente.')
                break
            else:
                to_overwrite = input(f'El archivo {filename} ya existe. ¿Desea sobreescribir? (S/N): ')
                if to_overwrite.upper() == 'N':
                    continue
                else:
                    os.remove(filename)
                    f = open(filename, 'wt')
                    f.close()
                    print(f'El fichero {filename} creado correctamente\n')
                    break
        elif '.xml' in extension:
            extension = extension[1:]
            if extension == '.xml':
                if not check_if_file_exists(filename):
                    root = ET.Element('test')
                    tree = ET.ElementTree(root)

                    with open(filename, 'wb') as f:
                        tree.write(f, encoding='utf-8', xml_declaration=True)
                        print(f'El fichero {filename} se ha creado correctamente\n')
                        break
                else:
                    to_overwrite = input(f'El archivo {filename} ya existe. ¿Desea sobreescribir? (S/N): ')
                    if to_overwrite.upper() == 'N':
                        continue
                    else:
                        os.remove(filename)

                        root = ET.Element('test')
                        tree = ET.ElementTree(root)
                        with open(filename, 'wb') as f:
                            tree.write(f, encoding='utf-8', xml_declaration=True)
                        print(f'El fichero {filename} se ha creado correctamente')
                        break
            else:
                print(f'El archivo {filename} tiene que tener extension ".json" o ".xml".')
                continue
    return filename


if __name__ == '__main__':
    create_file()
