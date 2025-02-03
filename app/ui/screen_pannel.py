from PySide6.QtWidgets import QWidget, QStackedLayout, QLabel

from app.view.user_screen import UserScreen


class ScreenPanel(QWidget):
    """ 우측 패널 (화면을 동적으로 변경 가능) """
    def __init__(self):
        super().__init__()

        # 스택형 레이아웃 생성 (화면 전환 가능)
        self.layout = QStackedLayout(self)
        self.setLayout(self.layout)

        self.user_screen = UserScreen()
        self.layout.addWidget(self.user_screen)
        self.layout.setCurrentWidget(self.user_screen)

        self.show()

    def set_screen(self, widget):
        """ 현재 화면을 변경하는 메서드 """
        # 기존 화면이 없는 경우, 추가한 후 첫 번째 화면으로 설정
        if widget not in [self.layout.itemAt(i).widget() for i in range(self.layout.count())]:
            self.layout.addWidget(widget)

        self.layout.setCurrentWidget(widget)
