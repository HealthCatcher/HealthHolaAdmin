from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from app.ui.left_panel import LeftPanel
from app.ui.screen_pannel import ScreenPanel
from app.screen.screen import Screen


class MainWindow(QMainWindow):
    """ 메인 윈도우: 좌측 패널과 우측 패널을 포함 """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modularized Main Window")

        # 메인 레이아웃 설정
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # 좌측 패널과 우측 패널 추가
        self.left_panel = LeftPanel()
        self.screen_panel = ScreenPanel()
        self.screen = Screen(self.screen_panel)

        main_layout.addWidget(self.left_panel, 1)   # 좌측 패널
        main_layout.addWidget(self.screen_panel, 4)  # 우측 패널 (더 넓게 설정)

        # 창 크기 설정
        self.setGeometry(100, 100, 800, 500)

        self.left_panel.button_clicked.connect(self.update_screen)

    def update_screen(self, name):
        self.screen.update_content(name)
