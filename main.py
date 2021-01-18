import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import QSize

from dir.setup import SetupFile


class MainWindow(QMainWindow):
    """
    Main window the application
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Password Manager")
        minSize = QSize(600, 600)
        self.setMinimumSize(minSize)

        self.setup = SetupFile()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()

    sys.exit(app.exec_())
