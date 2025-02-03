from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from app.screen import CouponScreen, ReportScreen, SurveyScreen, CommunityScreen, ExperienceScreen, UserScreen
from app.ui.left_panel import LeftPanel
from app.ui.screen_pannel import ScreenPanel


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

        main_layout.addWidget(self.left_panel, 1)   # 좌측 패널
        main_layout.addWidget(self.screen_panel, 4)  # 우측 패널 (더 넓게 설정)

        # 창 크기 설정
        self.setGeometry(100, 100, 800, 500)

        self.left_panel.button_clicked.connect(self.update_screen)

        self.screens = {}

        # 화면 클래스 매핑
        self.screen_classes = {
            "유저": UserScreen,
            "체험단": ExperienceScreen,
            "커뮤니티": CommunityScreen,
            "설문": SurveyScreen,
            "쿠폰": CouponScreen,
            "신고": ReportScreen
        }

    def update_screen(self, name):
        """ 버튼을 클릭하면 해당 화면을 생성하고 변경 """
        if name not in self.screens:
            # 화면을 처음 요청받으면 동적으로 인스턴스 생성
            self.screens[name] = self.screen_classes[name]()

        # ScreenPanel에 해당 화면을 설정
        self.screen_panel.set_screen(self.screens[name])
