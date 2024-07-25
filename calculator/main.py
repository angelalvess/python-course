from styles import setupTheme
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import sys
from main_window import MainWindow
from display import Display
from info import Info
from button import Button, ButtonsGrid


if __name__ == "__main__":
    app = QApplication(sys.argv)

    setupTheme(app)
    window = MainWindow()
    window.setWindowTitle("Calculator")

    info = Info()
    info.setText("0")
    window.WidgetToLayout(info)

    display = Display()
    display.setPlaceholderText("0")
    window.WidgetToLayout(display)

    grid = ButtonsGrid()
    window.vLayout.addLayout(grid)

    window.adjustFixedSize()

    window.show()

    app.exec()
