from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from app.screen.screen import Screen


class UserScreen(Screen):
    """ 유저 화면 (ScreenPanel에 표시될 위젯) """
    def __init__(self):
        super().__init__("유저 화면입니다.")
