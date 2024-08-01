from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.vLayout = QVBoxLayout()
        self.central_widget.setLayout(self.vLayout)

        self.setCentralWidget(self.central_widget)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def WidgetToLayout(self, widget):
        self.vLayout.addWidget(widget)

    def makeMessageBox(self):
        return QMessageBox(self)
