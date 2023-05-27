from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QLineEdit, QLabel, QRadioButton, QGridLayout
from PyQt5 import  QtGui, QtWidgets
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Создание поздравления")
        self.setGeometry(500, 550, 550, 500)

        self.main_text = QtWidgets.QLabel(self)
#кнопка
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(250, 200)
        self.btn.setText("Click")
        self.btn.setFixedWidth(100)
        self.btn.clicked.connect(self.click_btn)

#имя
        self.label = QLabel()
        self.qle = QLineEdit(self)
        self.qle.move(250, 150)
        self.qle.setFont(QtGui.QFont("Calibry", 12))
#праздник
        self.listwidget = QListWidget()
        pr = ['8 марта', '23 февраля', '1 апреля', '9 мая', 'годовщина', 'Новый год', 'День Рождения']
        self.listwidget.setFont(QtGui.QFont("Calibry", 14))
        self.listwidget.addItems(pr)
        self.listwidget.setFixedWidth(170)
        self.setCentralWidget(self.listwidget)
#цвет
        layout = QGridLayout()
        self.setLayout(layout)

        self.radiobutton = QRadioButton("red", self)
        self.radiobutton.move(250, 50)
        self.radiobutton.setChecked(True)
        self.radiobutton.color = "red"
        self.radiobutton.toggled.connect(self.onClicked)

        self.radiobutton = QRadioButton("green", self)
        self.radiobutton.move(250, 70)
        self.radiobutton.setChecked(True)
        self.radiobutton.color = "green"
        self.radiobutton.toggled.connect(self.onClicked)

        self.radiobutton = QRadioButton("blue", self)
        self.radiobutton.move(250, 90)
        self.radiobutton.setChecked(True)
        self.radiobutton.color = "blue"
        self.radiobutton.toggled.connect(self.onClicked)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            if radioButton.color == "red":
                self.main_text.setStyleSheet('color: rgb(255, 55, 55);')
            if radioButton.color == "green":
                self.main_text.setStyleSheet('color: rgb(55, 255, 55);')
            if radioButton.color == "blue":
                self.main_text.setStyleSheet('color: rgb(55, 55, 255);')

    def click_btn(self):
            name = self.qle.text()
            item = self.listwidget.currentItem()
            pr = item.text()
            Spr = {'8 марта': '8 марта', '23 февраля': '23 февраля', '1 апреля': '1 апреля', '9 мая': '9 мая',
                   'годовщина': 'годовщиной', 'Новый год': 'Новым годом', 'День Рождения': 'Днем Рождения'}
            self.main_text.setText("С " + Spr[pr] + ", " + name)
            self.main_text.setFont(QtGui.QFont("Calibry", 16))

            self.main_text.move(250, 300)
            self.main_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
