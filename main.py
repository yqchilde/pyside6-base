from PySide6.QtWidgets import QApplication, QWidget, QLabel


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.lb = QLabel('Hello World', self)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
