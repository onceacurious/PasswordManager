from PySide2.QtWidgets import *
from PySide2.QtCore import QPoint, QSize
from PySide2.QtGui import QCursor, QFont, QPixmap, Qt

from dir.stylesheet import *


class Authentication(QDialog):

    def __init__(self, *args, **kwargs):
        super(Authentication, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        size = QSize(300, 400)
        self.setFixedSize(size)
        self.setWindowOpacity(0.90)

        self.layout = QGridLayout(self)
        self.layout.setMargin(0)
        self.layout.setSpacing(0)

        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(auth)

        self.frame_layout = QGridLayout(self.frame)
        self.frame_layout.setMargin(0)
        self.frame_layout.setSpacing(0)
        
        self.left_frame = QFrame(self.frame)
        self.left_frame.setObjectName("left_frame")
        self.left_frame.setMaximumWidth(30)

        self.left_layout = QGridLayout(self.left_frame)
        self.left_layout.setMargin(0)
        self.left_layout.setSpacing(0)

        self.leftBtn_frame = QFrame(self.left_frame)
        self.leftBtn_frame.setObjectName("leftBtn_frame")
        self.leftBtn_frame.setFrameShape(QFrame.Panel)
        self.leftBtn_frame.setFrameShadow(QFrame.Sunken)
        # self.leftBtn_frame.setMinimumHeight(250)
        self.leftBtn_frame.setStyleSheet(auth)
        self.leftBtn_layout = QGridLayout(self.leftBtn_frame)
        self.leftBtn_layout.setSpacing(0)
        self.leftBtn_layout.setMargin(0)

        leftBtn = QFont()
        leftBtn.setPointSize(8)
        leftBtn.setFamily("Arial")
        leftBtn.setBold(True)
        self.in_btn = QPushButton(self.leftBtn_frame)
        self.in_btn.setText("L\nO\nG\nI\nN")
        self.in_btn.setFont(leftBtn)
        self.up_btn = QPushButton(self.leftBtn_frame)
        self.up_btn.setFont(leftBtn)
        self.up_btn.setText("R\nE\nG\nI\nS\nT\nE\nR")

        self.in_btn.setFlat(True)
        self.up_btn.setFlat(True)
        self.in_btn.setObjectName("in")
        self.up_btn.setObjectName("up")
        self.in_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.leftBtn_layout.addWidget(self.in_btn, 0, 0, 1, 1)
        self.leftBtn_layout.addWidget(self.up_btn, 1, 0, 1, 1)
        
        self.hallow_frame = QFrame(self.left_frame)

        self.left_layout.addWidget(self.leftBtn_frame, 0, 0, 1, 1)
        self.left_layout.addWidget(self.hallow_frame, 1, 0, 1, 1)
        
        self.right_frame = QFrame(self.frame)
        self.right_frame.setObjectName("right_frame")

        self.right_layout = QGridLayout(self.right_frame)
        self.right_layout.setMargin(0)
        self.right_layout.setSpacing(0)

        self.frame_layout.addWidget(self.left_frame, 0, 1, 1, 1)
        self.frame_layout.addWidget(self.right_frame, 0, 0, 1, 1)

        self.layout.addWidget(self.frame, 0, 0, 1, 1)

        self.oldPos = self.pos()

        self.mainFrame()

    def mainFrame(self):
        
        self.brandLogo_frame = QFrame(self.right_frame)
        self.brandLogo_layout = QGridLayout(self.brandLogo_frame)
        self.brandLogo_layout.setContentsMargins(5, 15, 5, 0)
        brandLogo = QPixmap(".\image\PM_logo.png")
        self.brandLogo_lbl = QLabel()
        self.brandLogo_lbl.setPixmap(brandLogo)
        self.brandLogo_lbl.setAlignment(Qt.AlignCenter)

        self.brandLogo_layout.addWidget(self.brandLogo_lbl, 0, 0, 1, 1)
        self.brandLbl_frame = QFrame(self.right_frame)
        self.brandLbl_layout = QGridLayout(self.brandLbl_frame)

        brand = "Password\nManager"
        brandFont = QFont()
        brandFont.setPointSize(15)
        brandFont.setLetterSpacing(QFont.AbsoluteSpacing, 2)
        brandFont.setBold(True)
        self.brand_lbl = QLabel(self.brandLbl_frame)
        self.brand_lbl.setObjectName("brand_lbl")
        self.brand_lbl.setText(brand.upper())
        self.brand_lbl.setAlignment(Qt.AlignCenter)
        self.brand_lbl.setFont(brandFont)

        dev = "Developed by:"
        devFont = QFont()
        devFont.setPointSize(12)
        devFont.setFamily("High Tower Text")
        self.dev_lbl = QLabel(self.brandLbl_frame)
        self.dev_lbl.setObjectName("dev_lbl")
        self.dev_lbl.setText(dev)
        self.dev_lbl.setFont(devFont)
        self.dev_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        name = "Innovative coding"
        nameFont = QFont()
        nameFont.setFamily("High Tower Text")
        nameFont.setPointSize(12)
        self.name_lbl = QLabel(self.brandLbl_frame)
        self.name_lbl.setObjectName("name_lbl")
        self.name_lbl.setText(name.title())
        self.name_lbl.setFont(nameFont)

        self.brandLbl_layout.addWidget(self.brand_lbl, 0, 0, 1, 2)
        self.brandLbl_layout.addWidget(self.dev_lbl, 1, 0, 1, 1)
        self.brandLbl_layout.addWidget(self.name_lbl, 1, 1, 1, 1)

        self.right_layout.addWidget(self.brandLogo_frame, 0, 0, 1, 1)
        self.right_layout.addWidget(self.brandLbl_frame, 1, 0, 1, 1)

    def loginFrame(self):
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
