from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from app.view.screen import Screen


class ExperienceScreen(Screen):
    def __init__(self):
        super().__init__("체험단")
