from app.screen.experience_screen import ExperienceScreen
from app.screen.user_screen import UserScreen


class Screen:
    """ 화면을 관리하는 클래스 (ScreenPanel의 콘텐츠 변경) """
    def __init__(self, screen_panel):
        self.screen_panel = screen_panel  # UI 패널 연결

        # 각 버튼과 연결될 화면 저장
        self.screens = {
            "유저": UserScreen(),
            "체험단": ExperienceScreen()
        }

    def update_content(self, screen_name):
        """ 화면을 변경하는 메서드 """
        if screen_name in self.screens:
            self.screen_panel.set_screen(self.screens[screen_name])
