from PySide6.QtWidgets import QWidget, QPushButton,QHBoxLayout,QMainWindow,QToolBar
from PySide6.QtCore import QSize

class RockWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rock Widget")
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction("New")

        quit_action=file_menu.addAction("wow")
        quit_action.triggered.connect(self.quit_app)

        toolbar=QToolBar()
        self.addToolBar(toolbar)
        toolbar.addAction("New")
        toolbar.addAction("Open")
        toolbar.addAction("Save")
        toolbar.addAction("Quit")
        toolbar.setIconSize(QSize(16,16))
        toolbar.actionTriggered.connect(self.quit_app)


        button = QPushButton("Click Me",self)
        button.move(100,100)
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)
        button.toggled.connect(self.button_toggled)
      



    def button_clicked(self):
        print("Button Clicked")

    def button_pressed(self):
        print("Button Pressed")

    def button_released(self):
        print("Button Released")

    def button_toggled(self):
        print("Button Toggled")            

    def quit_app(self):
        self.close()
        
        

       