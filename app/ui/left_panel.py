from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, Signal


class LeftPanel(QWidget):
    button_clicked = Signal(str)

    def __init__(self):
        super().__init__()
        self.setFixedWidth(200)  # 좌측 패널 너비 고정
        self.setStyleSheet("background-color: #2C3E50; border-right: 2px solid #1F2C38;")  # 배경색 & 테두리 추가
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(10)  # 버튼 간격 설정
        self.layout.setAlignment(Qt.AlignTop)  # 버튼을 상단 정렬

        buttons = ["유저", "체험단", "커뮤니티", "설문", "쿠폰"]
        self.buttons = []  # 버튼 리스트 저장

        for btn_label in buttons:
            button = QPushButton(btn_label)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFFFFF;
                    color: #333333;
                    font-size: 14px;
                    font-weight: 500;
                    border: 1px solid #DADCE0;
                    border-radius: 5px;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: #E8EAED;
                }
                QPushButton:pressed {
                    background-color: #D2D4D8;
                }
            """)

            button.clicked.connect(lambda checked, n=btn_label: self.button_clicked.emit(n))

            self.layout.addWidget(button)
            self.buttons.append(button)
