from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from app.screen.screen import Screen


class CommunityScreen(Screen):
    def __init__(self):
        super().__init__("커뮤니티 화면입니다.")