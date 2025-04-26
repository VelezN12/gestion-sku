from PyQt6.QtWidgets import QApplication

from gui.inicio import Inicio

class Sku():
    def __init__(self):
        self.app = QApplication([])
        self.inicio = Inicio()
        
        self.app.exec()