import sys
from PySide6.QtWidgets import QApplication, QDialog
from app.login_window import LoginScreen
from app.main_window import MainWindow  # 메인 창 클래스
from app.service.api_client import APIClient

if __name__ == "__main__":
    app = QApplication(sys.argv)
    api_client = APIClient()
    login_dialog = LoginScreen(api_client=api_client)
    if login_dialog.exec() == QDialog.Accepted:
        # 로그인 성공 시 MainWindow를 실행
        main_window = MainWindow(api_client)
        main_window.show()
        sys.exit(app.exec())
    else:
        sys.exit(0)