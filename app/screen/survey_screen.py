from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget

from app.screen.screen import Screen


class SurveyScreen(Screen):
    def __init__(self):
        super().__init__("설문 화면입니다.")