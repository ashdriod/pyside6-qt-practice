from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from api.weather_api import get_weather 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        
        self.location_input = QLineEdit(self)
        self.location_input.setPlaceholderText("Enter location")
        self.layout.addWidget(self.location_input)

        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.clicked.connect(self.fetch_weather)
        self.layout.addWidget(self.get_weather_button)

        self.weather_display = QLabel("Weather info will be displayed here", self)
        self.layout.addWidget(self.weather_display)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def fetch_weather(self):
        location = self.location_input.text()
        weather_info = get_weather(location)
        self.weather_display.setText(str(weather_info))
