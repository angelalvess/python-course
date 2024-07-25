from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("tranny World!")


button = QPushButton("Click me")
button2 = QPushButton("Click me")

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(button2)

central_widget.setLayout(layout)


def slot(status_bar):
    status_bar.showMessage("Button clicked")


def another_slot(checked):
    print('checked', checked)


status_bar = window.statusBar()
status_bar.showMessage("Hello, World!")

menu = window.menuBar()
file_menu = menu.addMenu("File")
add_action = file_menu.addAction("Add")
add_action.triggered.connect(lambda: slot(status_bar))

image_action = file_menu.addAction('Image')
image_action.setCheckable(True)
image_action.toggled.connect(another_slot)
window.show()

app.exec()
