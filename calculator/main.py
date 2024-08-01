import sys

from button import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from styles import setupTheme

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    setupTheme(app)
    window = MainWindow()
    window.setWindowTitle("Calculator")

    info = Info()
    info.setText("Sua conta")
    window.WidgetToLayout(info)

    display = Display()
    display.setPlaceholderText("0")
    window.WidgetToLayout(display)

    grid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(grid)

    window.adjustFixedSize()

    window.show()

    app.exec()
