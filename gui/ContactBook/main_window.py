from PySide6.QtWidgets import QMainWindow, QMessageBox,QProgressDialog,QWidget,QLabel,QVBoxLayout,QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from registration_window import RegistrationWindow   


# ... (other code remains the same)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to ContactBook")
        self.setFixedSize(400, 400)  # setting a fixed window dimensions
        self.setStyleSheet("background-color: lightgray;")

        # create a central widget and set it as the main window's central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
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

        # create a label for the heading
        self.label_heading = QLabel("Contact Book", self)
        self.label_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_heading.setStyleSheet("font-size: 45px; font-weight: bold; ")
        layout.addWidget(self.label_heading)

        # create a label for display message
        self.label_message = QLabel("No Registered Users !", self)
        self.label_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_message.setStyleSheet("font-size: 18px; font-style:italic; ")
        layout.addWidget(self.label_message)

        # create a button for registering a user
        button_register = QPushButton("Register User", self)
        button_register.setStyleSheet("font-size:18px")
        layout.addWidget(button_register, alignment=Qt.AlignmentFlag.AlignCenter)

        # create the button's clicked signal to a function
        button_register.clicked.connect(self.openRegistrationWindow)
    def openRegistrationWindow(self):
        """Opens the registration window."""
        registration_window = RegistrationWindow(self)  # Pass the main window as an argument to the registration window

        # Connect the userRegistered signal from the registration window to the startRegistration method of the main window
        registration_window.userRegistered.connect(self.startRegistration)

        registration_window.show()

    def startRegistration(self):
        # Get the user's input
        username = self.registration_window.input_username.text()
        password = self.registration_window.input_password.text()
        confirm_password = self.registration_window.input_confirm_password.text()

        if password != confirm_password:
            return

        # Create a progress dialog to show the registration progress
        self.progress_dialog = QProgressDialog("Registering User...", None, 0, 100, self)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setWindowTitle("Loading")
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)

        # Create a registration thread
        self.registration_thread = self.RegistrationThread(username, password)

        # Connect the progressChanged signal from the registration thread to the progress dialog
        self.registration_thread.progressChanged.connect(self.progress_dialog.setLabelText)

        # Connect the finished signal to the registrationFinished() method
        self.registration_thread.finished.connect(self.registrationFinished)

        # Start the registration thread
        self.registration_thread.start()

        # Show the progress dialog
        self.progress_dialog.show()
    def registrationFinished(self):
        # Hide the progress dialog
        self.progress_dialog.hide()

        # Check if the user has entered any information in the username and password fields.
        if not self.registration_window.input_username.text() or not self.registration_window.input_password.text():
            # Display an error message.
            QMessageBox.warning(self, "Error", "Please enter a username and password.")
            return

        # Update the label message
        self.label_message.setText("You have been registered!")

        # Show the main window again
        self.show()
