from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("欢迎来到主页"))
        self.setLayout(layout)
