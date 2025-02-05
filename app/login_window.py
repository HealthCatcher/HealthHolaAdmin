from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel

from app.service.api_client import APIClient


class LoginScreen(QDialog):
    def __init__(self, parent=None, api_client=None):
        super().__init__(parent)
        self.setWindowTitle("로그인")
        self.setup_ui()
        self.api_client = api_client or APIClient()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # 폼 레이아웃으로 아이디와 비밀번호 입력 필드를 배치
        form_layout = QFormLayout()
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)  # 비밀번호 입력 시 * 로 표시

        form_layout.addRow("아이디:", self.username_edit)
        form_layout.addRow("비밀번호:", self.password_edit)
        layout.addLayout(form_layout)

        # 로그인 버튼
        self.login_button = QPushButton("로그인")
        layout.addWidget(self.login_button)

        # 상태 메시지 표시용 라벨
        self.message_label = QLabel("")
        layout.addWidget(self.message_label)

        # 로그인 버튼 클릭 시 handle_login 메서드 호출
        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        success = self.api_client.login(username, password)
        if success:
            self.accept()
        else:
            self.message_label.setText("로그인 실패")
