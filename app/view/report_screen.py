from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from app.view.screen import Screen


class ReportScreen(Screen):
    def __init__(self):
        super().__init__("신고")