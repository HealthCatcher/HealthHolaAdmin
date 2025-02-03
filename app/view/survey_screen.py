from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget

from app.view.screen import Screen


class SurveyScreen(Screen):
    def __init__(self):
        super().__init__("설문")