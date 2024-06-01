from PySide6.QtWidgets import QWidget, QLineEdit,QHBoxLayout,QMainWindow,QLabel,QVBoxLayout,QPushButton,QTextEdit


class Day3side(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Day3side")

        label= QLabel("Hello World")
        self.line_edit= QLineEdit()

        button= QPushButton("Click Me")
        button.clicked.connect(self.button_click)
        self.text_holder= QLabel("Hello")


        self.text_edit = QTextEdit()  # Make text_edit an instance variable
        self.text_edit.setPlaceholderText("Enter your text here")
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)  # Pass the function reference
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)  # Pass the function reference
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)  # Pass the function reference
        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)  # Pass the function reference
        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)



        
        layout= QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.text_edit)
        layout.addWidget(copy_button)
        layout.addWidget(paste_button)
        layout.addWidget(clear_button)
        layout.addWidget(undo_button)
        layout.addWidget(redo_button)


        vlayout= QVBoxLayout()
        vlayout.addLayout(layout)
        vlayout.addWidget(button)
        vlayout.addWidget(self.text_holder)

        self.setLayout(vlayout)


    def button_click(self):
        self.text_holder.setText(self.line_edit.text())    

   