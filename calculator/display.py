from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variables import MINIMUM_WIDTH


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(
            """ font-size: 30px; padding: 10px; """)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MINIMUM_WIDTH)
