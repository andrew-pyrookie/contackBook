# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QWidget,QVBoxLayout,QLineEdit,QHBoxLayout,QSpacerItem,QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Registration Window")
        self.setFixedSize(400,400)
        self.setStyleSheet("background-color: lightgray;")
        
        # Create the central widget for the registration window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        #create a layout for the central widget
        layout=QVBoxLayout(central_widget)
        layout.setContentsMargins(0,0,0,0) # remove any margins
        
        # create a label for the registration window
        label = QLabel("Register User",self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 45px; font-weight: bold;")
        layout.addWidget(label)
        
        
        # Create the input boxes for username,passsword,confirm password
        input_username = QLineEdit()
        input_password = QLineEdit()
        input_confirm_password = QLineEdit()
        input_password.setEchoMode(QLineEdit.EchoMode.Password)
        input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        input_username.setPlaceholderText("Username")
        input_password.setPlaceholderText("Password")
        input_confirm_password.setPlaceholderText("Confirm Password")
        layout.addWidget(input_username)
        layout.addWidget(input_password)
        layout.addWidget(input_confirm_password)
        
        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)
        
        #create the register and back buttons
        button_register = QPushButton("Register",self)
        button_back = QPushButton("Back",self)
        button_register.setStyleSheet("font-size:18px")
        button_back.setStyleSheet("font-size:18px")
        
        # Add buttons to the button layout with proper alignments
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)
        button_layout.addWidget(button_register)
        button_layout.addWidget(button_back)
        
        # Set the alignments of the button layout
        layout.addWidget(button_register,alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(button_back,alignment=Qt.AlignmentFlag.AlignLeft)
        

    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to ContactBook")
        self.setFixedSize(400,400) # setting a fixed window dimensions
        self.setStyleSheet("background-color: lightgray;")
        
        #create a central widget and set it as the main window's central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        #Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0,0,0,0) # remove any margins
        
        # Create icon label
        icon_label = QLabel()
        pixmap = QPixmap("icon.svg")
        icon_label.setPixmap(pixmap)
        icon_label.setScaledContents(True) # scale the icon to fit the window
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon_label)
        
        #create a label for the heading
        self.label_heading = QLabel("Contact Book",self)
        self.label_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_heading.setStyleSheet("font-size: 45px; font-weight: bold; ")
        layout.addWidget(self.label_heading)
        
        
        #create a label for display message
        self.label_message = QLabel("No Registered Users !",self)
        self.label_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_message.setStyleSheet("font-size: 18px; font-style:italic; ")
        layout.addWidget(self.label_message)
        
        #create a button for registering a user
        button_register = QPushButton("Register User",self)
        button_register.setStyleSheet("font-size:18px")
        layout.addWidget(button_register,alignment=Qt.AlignmentFlag.AlignCenter)
        
        # create the button's clicked signal to a function
        button_register.clicked.connect(self.openRegistrationwindow)
        
    
    def openRegistrationwindow(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # ...
    sys.exit(app.exec())
