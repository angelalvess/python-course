import math
from typing import TYPE_CHECKING

from utils import isEmpty, isNumOrDot, isValidNumber
from variables import MEDIUM_FONT_SIZE

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


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
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ""
        self._equationInitial = "Sua conta"
        self._left = None
        self._right = None
        self._operator = None

        self.equation = self._equationInitial
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):

        self.display.eqPressed.connect(self._equal)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clearDisplay)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for row_number, row_values in enumerate(self._gridMask):

            for col_number, value in enumerate(row_values):

                button = Button(value)

                if not isNumOrDot(value) and not isEmpty(value):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, row_number, col_number)
                slot = self._makeSlot(
                    self._insertToDisplay, value)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        if text == 'C':
            self._connectButtonClicked(button, self._clearDisplay)

        if text == 'D':
            self._connectButtonClicked(
                button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button,
                                       self._invertNumber)

        if text in ['+', '-', '*', '/', '^']:
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOp, text))

        if text == '=':
            self._connectButtonClicked(
                button, self._equal)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _insertToDisplay(self, text):

        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        newValue = float(displayText) * - 1
        self.display.setText(str(newValue))

    def _clearDisplay(self):
        self._left = None
        self._right = None
        self._operator = None

        self.equation = self._equationInitial
        self.display.clear()

    def _configLeftOp(self, text):

        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError("Insert a number first")
            return

        if self._left is None:
            self._left = float(displayText)

        self._operator = text
        self.equation = f"{self._left} {self._operator} ??"

    @Slot()
    def _equal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError("Incomplete equation")
            return

        self._right = float(displayText)
        self.equation = f"{self._left} {self._operator} {self._right}"
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError("Zero division error")
        except OverflowError:
            self._showError("Overflow error")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

    def _showError(self, text):
        msgBox = self.window.makeMessageBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Question)
        msgBox.exec()
