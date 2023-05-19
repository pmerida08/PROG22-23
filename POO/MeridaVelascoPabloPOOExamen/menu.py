from cash_register import CashRegister


def main():
    menu = Menu("Entrada de caja (con la fecha y hora actual).", "Salida de caja (con la fecha y hora actual).",
                "Borrado del último movimiento de la caja.", "Impresión de la caja.", title="Caja Registradora")

    cash_register = CashRegister()

    while True:
        opc = menu.choose()
        match opc:
            case 1:
                cash_register.add(13.56, 'Gasoil')
            case 2:
                cash_register.add(-45.32, 'aAa1')
            case 3:
                cash_register.delete_last()
            case 4:
                print(cash_register)
            case _:
                break
    print("Hasta la próxima! :-)")


class Menu:

    def __init__(self, *options, title="Menú de opciones"):
        self.__options = list(options)
        self.__title = title

    @property
    def last_option(self):
        return len(self.__options)

    def choose(self):
        self.print_menu()
        return self.chosen_option()

    def print_menu(self):
        print(self.__title)
        print("-" * len(self.__title))
        for n in range(len(self.__options)):
            print(f"{n + 1}. {self.__options[n]}")
        print()

    def chosen_option(self):
        while True:
            opc = int(input("\nIntroduzca una opción: "))
            if 1 <= opc <= len(self.__options):
                return opc
            print("Ha introducido una opción incorrecta.")


if __name__ == '__main__':
    main()
