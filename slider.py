import sys
from PySide6.QtWidgets import QApplication, QSlider, QMainWindow

def response_to_slider(value):
    print(f"Slider value is {value}")



app = QApplication(sys.argv)
button=QSlider()
button.show()
sys.exit(app.exec())
