import sys
from PyQt6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt6.QtGui import QFont


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def function(self):
        print("Button was pressed")
        return "Hello"
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip("This is a <b>QWidget</b> widget")
        
        btn = QPushButton("Quit", self)
        btn.setToolTip("This is a quit button")
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QApplication.instance().quit)
        
        btn = QPushButton("Not quit", self)
        btn.setToolTip("This is a button")
        btn.resize(btn.sizeHint())
        btn.move(150, 50)
        btn.clicked.connect(self.function)
        
        self.setGeometry(450, 450, 450, 450)
        self.setWindowTitle("Testing PyQt6")
        self.show()

def main():
    
    app = QApplication(sys.argv)
    
    """
    w = QWidget()
    
    w.resize(600, 600)
    w.move(300, 300)
    w.setWindowTitle("Testing PyQt6")
    
    w.show()
    """
    
    win = Window()
    
    # runs sys.exit once window is closed
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()