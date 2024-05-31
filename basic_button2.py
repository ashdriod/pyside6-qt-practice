import sys
from PySide6.QtWidgets  import QApplication, QMainWindow, QPushButton


class buttonhelper(QMainWindow):

    def clickme(self):
        print("You clicked on the button ")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic PySide6 App")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        self.button = QPushButton("Click me", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.clickme)

app = QApplication(sys.argv)
window = buttonhelper()
window.show()
app.exec()