from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QFrame


class Screen(QWidget):
    def __init__(self, title="기본 화면"):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # 제목 레이블 (고정된 크기)
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; padding: 10px;")
        self.title_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)  # 제목 크기 고정
        self.layout.addWidget(self.title_label)

        # 스크린 영역 (실제 콘텐츠 표시)
        self.screen_area = QFrame()
        self.screen_area.setStyleSheet("background-color: white; border: 1px solid #DADCE0; padding: 10px;")
        self.screen_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 남은 공간을 모두 차지
        self.layout.addWidget(self.screen_area)

        self.screen_layout = QVBoxLayout(self.screen_area)
        self.screen_area.setLayout(self.screen_layout)

    def update_content(self, content):
        """ 화면 내용을 변경하는 공통 메서드 """
        self.title_label.setText(content)

    def clear_screen(self):
        while self.screen_layout.count():
            item = self.screen_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

