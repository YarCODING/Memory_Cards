from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtGui
import sys
from random import shuffle

app = QApplication([])

from layout_test import*
from layout_menu import*
from questions import questions, correct, wrong

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

window.setWindowIcon(QtGui.QIcon("icon.png"))
window_answer.setWindowIcon(QtGui.QIcon("icon.png"))
window_menu.setWindowIcon(QtGui.QIcon("menu_icon.jpg"))


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
questions[question_number].show(lb_question, rb1, rb2, rb3, rb4, question_number)

# функції для кнопок
def setNoChecked():
    group.setExclusive(False)
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    group.setExclusive(True)

def Answer():
    questions[question_number].check(rb1, rb2, rb3, rb4, lb_user_answer, lb_answer, lb_result)    
    window.hide()
    window_answer.show()

def Menu():
    window.hide()
    window_answer.hide()
    window_menu.show()

def showResult():
    global question_number, correct, wrong
    lb_finish_text.show()
    lb_right_number.setText(f'<h3 style="color: rgb(50,205,50);">Правильних: {correct}</h3>')
    lb_wrong_number.setText(f'<h3 style="color: rgb(250, 55, 55);">Неправильних: {wrong}</h3>')
    lb_right_number.show()
    lb_wrong_number.show()
    Menu()

    question_number = 0
    correct = 0
    wrong = 0

def Next():
    global question_number, correct, wrong
    window.show()
    window.resize(600, 500)
    window_answer.hide()
    setNoChecked()  
    question_number += 1
    try:
        questions[question_number].show(lb_question, rb1, rb2, rb3, rb4, question_number)
    # дії при закінченні питань
    except IndexError:
        showResult()

def Start_Return():
    window_menu.hide()
    window.show()


# підключення функцій до кнопок
btn_start.clicked.connect(Start_Return)
btn_answer.clicked.connect(Answer)
btn_next.clicked.connect(Next)
btn_menu.clicked.connect(Menu)
btn_exit.clicked.connect(lambda:sys.exit())

# запуск додатку
app.exec_()