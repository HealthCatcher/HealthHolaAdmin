from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from app.view.screen import Screen


class CommunityScreen(Screen):
    def __init__(self):
        super().__init__("커뮤니티")