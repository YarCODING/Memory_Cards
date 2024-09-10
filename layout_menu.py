from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

btn_start = QPushButton("Почати тестування")
btn_learning = QPushButton("Редагування питаннь")
btn_exit = QPushButton("Вийти")

main_line_menu = QVBoxLayout()
main_line_menu.addWidget(btn_start, alignment=Qt.AlignCenter)
main_line_menu.addWidget(btn_learning, alignment=Qt.AlignCenter)
main_line_menu.addWidget(btn_exit, alignment=Qt.AlignCenter)