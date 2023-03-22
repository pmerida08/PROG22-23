from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Es buenisima esta app')

        self.button = QPushButton('Presione aquí')
        self.button.clicked.connect(self.gay)
        self.setCentralWidget(self.button)

    def gay(self):
        self.button.setText("Ta guapo eh")
        self.button.setEnabled(False)

        self.setWindowTitle("TE LO DIJE :D")

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec_()