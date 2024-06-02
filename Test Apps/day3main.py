from PySide6.QtWidgets import QApplication
from day3side import Day3side
import sys

app = QApplication(sys.argv)
window= Day3side()
window.show()
app.exec()

