from PySide6.QtWidgets import QWidget, QProgressBar, QVBoxLayout, QLabel

class UpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("正在更新")
        self.label = QLabel("下载中...")
        self.progress = QProgressBar()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.progress)
        self.setLayout(layout)

    def update_progress(self, value, total):
        percent = int(value / total * 100)
        self.progress.setValue(percent)
