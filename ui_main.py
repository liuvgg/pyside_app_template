from PySide6.QtWidgets import QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout
from pages.page_home import HomePage
from pages.page_settings import SettingsPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 App Template")

        # 页面堆叠
        self.stack = QStackedWidget()
        self.home_page = HomePage()
        self.settings_page = SettingsPage()
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.settings_page)

        # 控制按钮
        nav = QWidget()
        layout = QVBoxLayout(nav)
        btn_home = QPushButton("主页")
        btn_settings = QPushButton("设置")
        layout.addWidget(btn_home)
        layout.addWidget(btn_settings)
        btn_home.clicked.connect(lambda: self.stack.setCurrentWidget(self.home_page))
        btn_settings.clicked.connect(lambda: self.stack.setCurrentWidget(self.settings_page))

        # 主布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(nav)
        main_layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
