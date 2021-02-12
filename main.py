# This Python file uses the following encoding: utf-8
from PySide2.QtCore import QObject, QUrl, Slot, Signal
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class Backend(QObject):
    """Создаем сигнал для QML"""
    lableSignal = Signal(str)

    def __init__(self):
        super(Backend, self).__init__()
        self.var = 0

    @Slot(str)
    def click_button1(self, text):
        self.var += 1
        print("Python", text, 'var', self.var)
        self.lableSignal.emit(str(self.var))

    @Slot(str)
    def click_button2(self, text):
        self.var -= 1
        print("Python", text, 'var', self.var)
        self.lableSignal.emit(str(self.var))


if __name__ == "__main__":
    import os
    import sys

    app = QGuiApplication()
    backend = Backend()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("backend", backend)
    qml_file = "main.qml"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(current_dir, qml_file)
    engine.load(QUrl.fromLocalFile(filename))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
