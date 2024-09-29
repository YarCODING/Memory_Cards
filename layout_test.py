from PyQt5.QtWidgets import QPushButton, QRadioButton, QLabel, QSpinBox, QGroupBox, QButtonGroup, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
lb_timer = QLabel('0')
spin = QSpinBox()
spin.setValue(30)


#питання
btn_answer = QPushButton("Відповісти")
lb_question = QLabel("Питання")

rb1 = QRadioButton('1 варіант')
rb2 = QRadioButton('2 варіант')
rb3 = QRadioButton('3 варіант')
rb4 = QRadioButton('4 варіант')

group = QButtonGroup()
group.addButton(rb1, 1)
group.addButton(rb2, 2)
group.addButton(rb3, 3)
group.addButton(rb4, 4)

rbuttons = [rb1, rb2, rb3, rb4]

groupbox = QGroupBox("Варіанти відповідей")

line = QHBoxLayout(groupbox)
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineV1.addWidget(rb1)
lineV1.addWidget(rb3)
lineV2.addWidget(rb2)
lineV2.addWidget(rb4)
line.addLayout(lineV1)
line.addLayout(lineV2)

main_line_test = QVBoxLayout()
line1_test = QHBoxLayout()
line2_test = QHBoxLayout()
line3_test = QHBoxLayout()
line4_test = QHBoxLayout()

line1_test.addWidget(btn_menu)
line1_test.addWidget(lb_timer)
line1_test.addWidget(btn_rest)
line1_test.addWidget(spin)

line2_test.addWidget(lb_question)
line3_test.addWidget(groupbox)                 
line4_test.addWidget(btn_answer)

main_line_test.addLayout(line1_test)
main_line_test.addLayout(line2_test)
main_line_test.addLayout(line3_test)                         
main_line_test.addLayout(line4_test)



#відповіді
lb_user_answer_text = QLabel('Ваша відповідь')
lb_user_answer = QLabel('Відповіді не має')

btn_next = QPushButton("Наступне питання")

groupbox_answer = QGroupBox("Правильна відповідь")
lb_answer = QLabel("Правильна відповідь")
lb_result = QLabel('___')

main_line_answer = QVBoxLayout()
main_line_answer.addLayout(line1_test)
main_line_answer.addWidget(lb_user_answer_text)
main_line_answer.addWidget(lb_user_answer)
line_answer = QVBoxLayout(groupbox_answer)
line_answer.addWidget(lb_answer)
main_line_answer.addWidget(groupbox_answer)
main_line_answer.addWidget(lb_result)
main_line_answer.addWidget(btn_next)
main_line_answer.addLayout(line_answer)