from PyQt5.QtWidgets import QWidget, QApplication
import sys
from random import shuffle

app = QApplication([])

from layout_test import*
from layout_menu import*
from questions import*

# налаштування вікон
window = QWidget()
window_answer = QWidget()
window_menu = QWidget()

window.resize(600, 500)
window_answer.resize(600, 500)
window_menu.resize(200, 200)

window.setWindowTitle('Memory Cards')
window_answer.setWindowTitle('Memory Cards-Answer')
window_menu.setWindowTitle('Memory Cards-Menu')

# додавання лейаутів у вікно
window.setLayout(main_line_test)
window_answer.setLayout(main_line_answer)
window_menu.setLayout(main_line_menu)

# початкова відимість вікон
window.show()
window_answer.hide()
window_menu.hide()

# перемішування питань
shuffle(questions)
question_number = 0
questions[question_number].show(lb_question, rb1, rb2, rb3, rb4)

# функції для кнопок
def Answer():
    window.hide()
    window_answer.show()

def Menu():
    window.hide()
    window_answer.hide()
    window_menu.show()

def Next():
    global question_number
    window.show()
    window.resize(600, 500)
    window_answer.hide()
    question_number += 1

    try:
        questions[question_number].show(lb_question, rb1, rb2, rb3, rb4)
    except IndexError:
        lb_finish_text.show()
        Menu()


# підключення функцій до кнопок
btn_answer.clicked.connect(Answer)
btn_next.clicked.connect(Next)
btn_menu.clicked.connect(Menu)
btn_exit.clicked.connect(lambda:sys.exit())

# запуск додатку
app.exec_()