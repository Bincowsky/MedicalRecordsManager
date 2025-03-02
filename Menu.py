import sys


from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        # Add widgets to the layout
        
        button1 = QPushButton("Medical Form", self) 
        layout.addWidget(button1)
        layout.addWidget(QPushButton("Statistics"))
        layout.addWidget(QPushButton("Server-Push"))
        layout.addStretch()
        # Set the layout on the application's window
        
         
        
        self.setLayout(layout)
        
        button1.clicked.connect(self.clickme)
    def clickme(self): 
  
        # printing pressed 
        print("pressed")
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())