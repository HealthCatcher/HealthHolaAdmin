from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from app.screen.screen import Screen


class ReportScreen(Screen):
    def __init__(self):
        super().__init__("신고 내역 화면입니다.")