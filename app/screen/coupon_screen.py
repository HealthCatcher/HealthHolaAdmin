from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from app.screen.screen import Screen


class CouponScreen(Screen):
    def __init__(self):
        super().__init__("쿠폰 화면입니다.")