from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

from app.view.screen import Screen


class UserScreen(Screen):
    def __init__(self):
        super().__init__("유저 화면")  # 제목 설정
        self.setup_ui()

    def setup_ui(self):
        """ 스크린 영역에 새로운 UI 요소 추가 """
        self.clear_screen()  # 기존 UI 초기화

        # 레이아웃 설정
        layout = self.screen_layout  # 부모 클래스에서 제공하는 레이아웃 사용

        # ✅ 버튼이 지역 변수로만 존재하면 GC가 제거할 가능성이 있으므로, self.button으로 저장
        self.user_label = QLabel("유저 화면 콘텐츠")
        self.user_label.setStyleSheet("font-size: 14px; padding: 5px;")
        layout.addWidget(self.user_label)

        # ✅ 버튼을 self.button으로 저장하여 가비지 컬렉터 방지
        self.button = QPushButton("유저 버튼")
        self.button.clicked.connect(self.on_button_click)  # ✅ 버튼 클릭 이벤트 연결
        layout.addWidget(self.button)

    def on_button_click(self):
        """ 버튼 클릭 시 동작하는 메서드 """
        self.user_label.setText("버튼이 클릭됨!")