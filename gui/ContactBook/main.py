import sys
from PySide6.QtWidgets import QApplication, QProgressDialog
from PySide6.QtCore import Qt
from registration_window import RegistrationWindow
from main_window import MainWindow

# ... (other code remains the same)

import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

def main():
    """The main function."""

    # Create the main window.
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
