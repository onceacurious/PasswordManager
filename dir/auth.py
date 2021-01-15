from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QSize


class Authentication(QDialog):

    def __init__(self, *args, **kwargs):
        super(Authentication, self).__init__(*args, **kwargs)
        self.setWindowTitle("User Authentication")
        size = QSize(200, 300)
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.setWindowOpacity(0.80)
