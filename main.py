from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication([])

from layout_test import*

window = QWidget()
window_answer = QWidget()

window.resize(600, 500)
window_answer.resize(600, 500)

window.setWindowTitle('Memory Cards')
window_answer.setWindowTitle('Memory Cards Answer')

window.setLayout(main_line_test)
window_answer.setLayout(main_line_answer)

window.show()
window_answer.hide()

def Answer():
    window.hide()
    window_answer.show()
def Next():
    window.show()
    window_answer.hide()

btn_answer.clicked.connect(Answer)
btn_next.clicked.connect(Next)

app.exec_()