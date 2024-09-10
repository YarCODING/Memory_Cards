from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication([])

from layout_test import*
from layout_menu import*

window = QWidget()
window_answer = QWidget()
window_menu = QWidget()

window.resize(600, 500)
window_answer.resize(600, 500)
window_menu.resize(200, 200)

window.setWindowTitle('Memory Cards')
window_answer.setWindowTitle('Memory Cards-Answer')
window_menu.setWindowTitle('Memory Cards-Menu')

window.setLayout(main_line_test)
window_answer.setLayout(main_line_answer)
window_menu.setLayout(main_line_menu)

window.show()
window_answer.hide()
window_menu.hide()

def Answer():
    window.hide()
    window_answer.show()
def Next():
    window.show()
    window_answer.hide()
def Menu():
    window.hide()
    window_answer.hide()
    window_menu.show()

btn_answer.clicked.connect(Answer)
btn_next.clicked.connect(Next)
btn_menu.clicked.connect(Menu)

app.exec_()