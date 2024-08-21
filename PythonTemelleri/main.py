import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

class Backend(QObject):
    clicked = Signal()

    @Slot()
    def on_button_clicked(self):
        print("Button clicked in Python!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the backend object
    backend = Backend()

    # Load the QML file
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("pyButton", backend)
    engine.load("main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    # Connect the signal
    backend.clicked.connect(backend.on_button_clicked)

    sys.exit(app.exec())
