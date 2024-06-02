from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider

def button_clicked(data):
    print("Button clicked", data)


def responsetoslider(value):
    print("Slider value: ", value)

app = QApplication()
button=QPushButton("Click me")
slider=QSlider(Qt.Horizontal)
button.clicked.connect(button_clicked)
button.setCheckable(True)
slider.valueChanged.connect(responsetoslider)
slider.show()
app.exec()