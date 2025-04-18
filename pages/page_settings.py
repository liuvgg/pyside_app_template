from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("这里是设置页"))
        self.setLayout(layout)
