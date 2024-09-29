from PyQt5.QtWidgets import QWidget, QApplication
from threading import Thread
from PyQt5 import QtGui
import sys
from random import shuffle

app = QApplication([])

from layout_test import*
from layout_menu import*
from questions import questions, correct, wrong

import os, time
clear = lambda: os.system('cls')

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
questions[question_number].show(lb_question, rbuttons, question_number)


# функції для кнопок
clear()
def setNoChecked():
    group.setExclusive(False)
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    group.setExclusive(True)

def Answer():
    questions[question_number].check(lb_user_answer, rbuttons, lb_answer, lb_result)    
    window.hide()
    window_answer.show()

def Menu():
    window_menu.show()
    window.hide()
    window_answer.hide()

def Next():
    global question_number, correct, wrong
    window.show()
    window.resize(600, 500)
    window_answer.hide()
    setNoChecked()  
    question_number += 1
    try:
        shuffle(rbuttons)
        questions[question_number].show(lb_question, rbuttons, question_number)
    # дії при закінченні питань
    except IndexError:
        questions[question_number-1].showEndResult(lb_right_number, lb_wrong_number, lb_finish_text)
        Menu()

        question_number = 0
        correct = 0
        wrong = 0

def Start_Return():
    global TimerWork
    window_menu.hide()
    window.show()  

def Exit():
    global TimerWork
    TimerWork = False
    sys.exit()


# секундомер
sec = 0
TimerWork =True

def timer():
    global sec, clear, TimerWork
    while TimerWork:
        lb_timer.setText(f'Таймер: {sec}')
        time.sleep(1)
        clear()
        sec += 1
    
        if not(window.isVisible()) and not(window_answer.isVisible()) and not(window_menu.isVisible()):
            TimerWork = False
            sys.exit()

th = Thread(target=timer)
th.start()

# підключення функцій до кнопок
btn_start.clicked.connect(Start_Return)
btn_answer.clicked.connect(Answer)
btn_next.clicked.connect(Next)
btn_menu.clicked.connect(Menu)
btn_exit.clicked.connect(Exit)


# запуск додатку
app.exec_()