from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])



main_win = QWidget()
main_win.setWindowTitle("Victory")
main_win.resize(500, 200)




lbl = QLabel("Вякому році канал отримав «золоту кнопку» від Youtube")

btn1 = QRadioButton("2005")
btn2 = QRadioButton("2010")
btn3 = QRadioButton("2015")
btn4 = QRadioButton("2020")

main_layout = QVBoxLayout()
main_layout.addWidget(lbl)

row1_layout = QHBoxLayout()
row2_layout = QHBoxLayout()

row1_layout.addWidget(btn1)
row1_layout.addWidget(btn2)

row2_layout.addWidget(btn3)
row2_layout.addWidget(btn4)

main_layout.addLayout(row1_layout)
main_layout.addLayout(row2_layout)

def show_right():
    win_info = QMessageBox(main_win)
    win_info.setWindowTitle("Result")
    win_info.setText("Правильна відповідь!")
    win_info.show()

def show_wrong():
    win_info = QMessageBox(main_win)
    win_info.setWindowTitle("Result")
    win_info.setText("Неправильна відповідь!")
    win_info.show()

btn1.clicked.connect(show_wrong)
btn2.clicked.connect(show_wrong)
btn3.clicked.connect(show_right)
btn4.clicked.connect(show_wrong)


main_win.setLayout(main_layout)
main_win.show()
app.exec()