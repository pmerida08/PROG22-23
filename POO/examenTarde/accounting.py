from typing import Union
from datetime import datetime
import csv


class Apuntes:
    def __init__(self, concepto, importe, numero: str = None, fecha: datetime = datetime.now()):
        __ultimo_numero = 0
        with open('apuntes.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for a in csv_reader:
                if a[0] == numero:
                    raise ApunteYaRegistrado('El apunte ya está registrado.')
                __ultimo_numero = int(a[0])

        self.__numero = __ultimo_numero + 1
        self.__concepto = concepto
        self.__importe = importe
        self.__fecha = fecha

        with open('apuntes.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',', quotechar='"')
            csv_writer.writerow([self.__numero, self.__concepto, self.__importe, self.__fecha])

    # TODO
    def exportar_apuntes(self):   # No me funciona bien lo que tenía
        pass

    def __str__(self):
        return f"Apunte {self.__numero}: ** Concepto: {self.__concepto} ** Importe: {self.__importe} € " \
               f"** Fecha/Hora: {self.__fecha}"


class Empresa:
    __empresas_cifs = []

    def __init__(self, cif: str, nombre: str, direccion: str, apuntes: list[Union[str, Apuntes]]):
        if cif in Empresa.__empresas_cifs:
            raise EmpresaRegistrada('Esta empresa ya ha sido registrada.')

        self.__cif = cif
        self.__nombre = nombre
        self.__direccion = direccion
        self.__apuntes = apuntes

    def registrar_ingreso(self, concepto, importe):
        if importe < 0:
            raise ValueError('El importe del ingreso debería ser positivo')
        self.__apuntes.append(Apuntes(concepto=concepto, importe=importe))

    def registrar_gasto(self, concepto, importe):
        if importe > 0:
            raise ValueError('El importe del gasto debería ser negativo')
        self.__apuntes.append(Apuntes(concepto=concepto, importe=importe))

    @staticmethod
    def balance():
        with open('apuntes.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            total = 0
            for a in csv_reader:
                total += float(a[2])
        print(total)

    @staticmethod
    def eliminar_duplicados():  # No funciona bien
        filas = set()
        with open('apuntes.csv', 'r', encoding='utf-8', newline='') as file:
            csv_reader = csv.reader(file)
            cabecera = next(csv_reader)
            for f in csv_reader:
                filas.add(tuple(f))

        with open('apuntes.csv', 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(cabecera)
            for f in filas:
                csv_writer.writerow(f)

    def __str__(self):
        apuntes_str = "\n".join(str(apunte) for apunte in self.__apuntes)
        return f"---------------------------------------------\n" \
               f"EMPRESA: {self.__cif}      {self.__nombre}\n" \
               f"DOMICILIO {self.__direccion}\n" \
               f"---------------------------------------------\n" \
               f"APUNTES:\n{apuntes_str}" \



class EmpresaRegistrada(Exception):
    pass


class ApunteYaRegistrado(Exception):
    pass


if __name__ == '__main__':
    a1 = Apuntes('Coche', '-18.8')
    a2 = Apuntes('Carrito', '-98.9')
    a3 = Apuntes('Bizum pago mes', '250.8')
    a4 = Apuntes('Bizum pago mes', '250.8')
    emp = Empresa('454334535', 'IESS', 'C/ AAAAA', [a1, a2, a3, a4])
    print(emp)
