from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmptry


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPointSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(70, 70)


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for row_number, row_values in enumerate(self._gridMask):

            for col_number, value in enumerate(row_values):

                button = Button(value)

                if not isNumOrDot(value) and not isEmptry(value):
                    button.setProperty("cssClass", "specialButton")

                self.addWidget(button, row_number, col_number)
