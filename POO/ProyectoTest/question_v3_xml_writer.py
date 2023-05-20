import xml.etree.ElementTree as ET
from xml.dom import minidom

MAX_OPTIONS = 4
XML_FILE = 'questions.xml'

tree = ET.parse(XML_FILE)
root = tree.getroot()

# Escribiendo las preguntas y sus opciones

question = ET.SubElement(root, 'question', {'points': '1'})
statement = ET.SubElement(question, 'statement')
statement.text = input(f'Pregunta para añadir: ')
options = ET.SubElement(question, 'options')
for o in range(1, MAX_OPTIONS + 1):
    option = ET.SubElement(options, 'option', {'points': '-0.25'})
    option.text = input(f'Opcion {o}: ')


tree = ET.ElementTree(root)
tree.write('questions.xml', encoding='unicode')

# Para poner el archivo 'xml' bonito
xml_str = minidom.parseString(ET.tostring(root)).toprettyxml()

with open("questions.xml", "w") as f:
    f.write(xml_str)
