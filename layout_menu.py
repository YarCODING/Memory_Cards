from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

lb_finish_text = QLabel('Питання закінчились')
lb_right_number = QLabel('Правильних: ?')
lb_wrong_number = QLabel('Неправильних: ?')

btn_start = QPushButton("Почати/продовжити тестування")
btn_learning = QPushButton("Редагування питаннь(не працює)")
btn_exit = QPushButton("Вийти")

main_line_menu = QVBoxLayout()
main_line_menu.addWidget(lb_finish_text, alignment=Qt.AlignCenter)
main_line_menu.addWidget(lb_right_number)
main_line_menu.addWidget(lb_wrong_number)
main_line_menu.addWidget(btn_start, alignment=Qt.AlignCenter)
main_line_menu.addWidget(btn_learning, alignment=Qt.AlignCenter)
main_line_menu.addWidget(btn_exit, alignment=Qt.AlignCenter)

lb_finish_text.hide()
lb_right_number.hide()
lb_wrong_number.hide()