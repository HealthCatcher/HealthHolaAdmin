from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Screen(QWidget):
    def __init__(self, title="기본 화면"):
        super().__init__()

        # 기본 레이아웃 설정
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # 화면 제목 설정
        self.title_label = QLabel(title)
        self.layout.addWidget(self.title_label)

        # 기본 스타일 적용
        self.setStyleSheet("background-color: white; font-size: 16px; padding: 20px;")

    def update_content(self, content):
        """ 화면 내용을 변경하는 공통 메서드 """
        self.title_label.setText(content)
