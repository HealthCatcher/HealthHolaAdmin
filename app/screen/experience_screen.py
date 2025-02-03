from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from app.screen.screen import Screen


class ExperienceScreen(Screen):
    def __init__(self):
        super().__init__("체험단 화면입니다.")
