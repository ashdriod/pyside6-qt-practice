import sys
from PySide6.QtWidgets  import QApplication, QMainWindow, QPushButton



class buttonholder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic PySide6 App")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        self.button = QPushButton("Click me", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.clickme)

    def clickme(self):
        self.button.setText("You clicked me")




app = QApplication(sys.argv)
window = buttonholder()
window.show()
sys.exit(app.exec())