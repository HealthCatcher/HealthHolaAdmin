from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class UserScreen(QWidget):
    """ 유저 화면 (ScreenPanel에 표시될 위젯) """
    def __init__(self):
        super().__init__()

        # 수직 레이아웃 생성
        layout = QVBoxLayout(self)
        self.label = QLabel("유저 화면입니다.")
        layout.addWidget(self.label)

        # 스타일 설정
        self.setStyleSheet("background-color: white; font-size: 16px; padding: 20px;")
