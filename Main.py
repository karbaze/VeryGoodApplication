from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

lbl = QLabel("Текст")
btn = QPushButton("Кнопка типа")

main_Loyout = QVBoxLayout()
main_Loyout.addWidget(lbl)
main_Loyout.addWidget(btn)

window.setLayout(main_Loyout)
window.show()
app.exec()