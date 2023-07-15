import csv
import xlsxwriter
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox,QWidget
from PySide6.QtCore import Qt, QThread, Signal

class RegistrationWindow(QDialog):
    class RegistrationThread(QThread):
        progressChanged = Signal(str)

        def __init__(self, username, password):
            super().__init__()
            self.username = username
            self.password = password
            self.progressChanged = Signal(str)

        def run(self):
            # Save the user's input to a CSV file
            with open('users.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([self.username, self.password])

            # Simulate some time-consuming task
            import time
            progress = 0
            while progress < 100:
                time.sleep(0.1)
                progress += 10
                self.progressChanged.emit(f"Creating spreadsheet... {progress}%")

            # Create a spreadsheet file
            workbook = xlsxwriter.Workbook(f'{self.username}.xlsx')
            worksheet = workbook.active

            # Add the headers to the spreadsheet
            worksheet.write('A1', 'Name')
            worksheet.write('B1', 'Email Address')
            worksheet.write('C1', 'Phone Number')
            worksheet.write('D1', 'Address')
            worksheet.write('E1', 'Company')

            # Save the spreadsheet file
            workbook.save()

            # Complete the registration process
            self.progressChanged.emit("Registration complete.")

    def __init__(self, main_window=None):
        super().__init__()

        self.setWindowTitle("Register User")
        self.setFixedSize(400, 400)
        self.setStyleSheet("background-color: lightgray;")

        # Store the main window object
        self.main_window = main_window

        # Create the central widget for the registration window
        central_widget = QWidget(self)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # remove any margins

        # Create a label for the registration window
        label = QLabel("Register User", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 45px; font-weight: bold;")
        layout.addWidget(label)

        # Create the input boxes for username, password, confirm password
        self.input_username = QLineEdit()
        self.input_password = QLineEdit()
        self.input_confirm_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_username.setPlaceholderText("Username")
        self.input_password.setPlaceholderText("Password")
        self.input_confirm_password.setPlaceholderText("Confirm Password")
        layout.addWidget(self.input_username)
        layout.addWidget(self.input_password)
        layout.addWidget(self.input_confirm_password)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Create the register and back buttons
        button_register = QPushButton("Register", self)
        button_back = QPushButton("Back", self)
        button_register.setStyleSheet("font-size: 18px")
        button_back.setStyleSheet("font-size: 18px")

        # Add buttons to the button layout with proper alignments
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
       

        button_layout.addItem(spacer)
        button_layout.addWidget(button_register)
        button_layout.addWidget(button_back)

        # Set the alignments of the button layout
        layout.addWidget(button_register, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignLeft)

        # Connect the back button to the goBackToMainWindow() method
        button_back.clicked.connect(self.goBackToMainWindow)

        # Create a registration thread instance
        self.registration_thread = None

    def goBackToMainWindow(self):
        if self.main_window:
            self.main_window.show()
        self.hide()

    def register_user(self):
        # Get the user's input
        username = self.input_username.text()
        password = self.input_password.text()
        confirm_password = self.input_confirm_password.text()

        if password != confirm_password:
            return

        # Create a registration thread if not already created
        if not self.registration_thread:
            self.registration_thread = self.RegistrationThread(username, password)
            # Connect the progressChanged signal to the progress dialog
            self.registration_thread.progressChanged.connect(self.progress_dialog.setLabelText)
            # Connect the finished signal to the registrationFinished() function
            self.registration_thread.finished.connect(self.registrationFinished)
            # Start the registration thread
            self.registration_thread.start()

    def registrationFinished(self):
        # Hide the progress dialog
        self.progress_dialog.hide()

        # Check if the user has entered any information in the username and password fields.
        if not self.input_username.text() or not self.input_password.text():
        # Display an error message.
            QMessageBox.warning(self, "Error", "Please enter a username and password.")
            return

        
        # Update the label message
        self.label_message.setText("You have been registered!")
        
        self.show()