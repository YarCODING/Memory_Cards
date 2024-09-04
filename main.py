from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication([])

from layout_test import*

window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Cards')
window.setLayout(main_line_test)
window.show()


app.exec_()