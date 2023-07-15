from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from registration_window import RegistrationWindow   


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
        layout.setContentsMargins(0, 0, 0, 0)  # remove any margins

        # Create icon label
        icon_label = QLabel()
        pixmap = QPixmap("icon.svg")
        icon_label.setPixmap(pixmap)
        icon_label.setFixedSize(96, 96)  # set the icon size to 96x96
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

         # Add the icon and label to the layout
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
        button_register.clicked.connect(self.openRegistrationWindow)
        
    
    def openRegistrationWindow(self):
        """Opens the registration window."""
        registration_window = RegistrationWindow()

        
        registration_window.show()
        self.hide()