import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Professional Calculator")
        self.setGeometry(100, 100, 400, 600)

        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        
        self.display = QLineEdit(self)
        self.display.setFixedHeight(80)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("Arial", 24))
        layout.addWidget(self.display)

        
        button_layout = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "=", "/"
        ]

        grid_layout = QGridLayout()
        row, col = 1, 0
        self.button_dict = {} 

        for button_text in button_layout:
            button = QPushButton(button_text, self)
            button.setFixedSize(80, 80)
            button.setFont(QFont("Arial", 18))
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
            self.button_dict[button_text] = button  # Store button in the dictionary

        layout.addLayout(grid_layout)
        central_widget.setLayout(layout)

        
        for button_text in button_layout:
            if button_text == "=":
                continue
            button = self.button_dict.get(button_text)
            if button:
                button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        button = self.sender()
        if button:
            current_text = self.display.text()
            button_text = button.text()

            if button_text == "=":
                try:
                    result = eval(current_text)
                    self.display.setText(str(result))
                except Exception as e:
                    self.display.setText("Error")
            else:
                self.display.setText(current_text + button_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
