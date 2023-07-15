import sys
from PySide6.QtWidgets import QApplication, QProgressDialog
from PySide6.QtCore import Qt
from registration_window import RegistrationWindow
from main_window import MainWindow

def main():
    """The main function."""

    # Create the main window.
    app = QApplication(sys.argv)
    window = MainWindow()

    # Create a QProgressDialog to show the loading signal
    progress_dialog = QProgressDialog("Registering User...", None, 0, 100, window)
    progress_dialog.setWindowModality(Qt.WindowModal)
    progress_dialog.setWindowTitle("Loading")
    progress_dialog.setCancelButton(None)
    progress_dialog.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)

    # Create the registration window.
    registration_window = RegistrationWindow()

    # Connect the progressChanged signal to the progress dialog.
        # Connect the progressChanged signal from the registration thread to the progress dialog.
    registration_window.registration_thread.progressChanged.connect(progress_dialog.setLabelText)


    # Connect the finished signal to the registrationFinished() function.
    registration_window.finished.connect(progress_dialog.hide)

    # Open the registration window.
    registration_window.show()
    window.hide()

    # Start the registration thread.
    registration_window.registration_thread.start()

    # When the progressChanged signal is emitted, update the label text in the progress dialog.
    while registration_window.registration_thread.isRunning():
        progress = registration_window.registration_thread.progressChanged.emit()
        progress_dialog.setLabelText(progress)

    # When the registration thread is finished, hide the progress dialog.
    progress_dialog.hide()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
