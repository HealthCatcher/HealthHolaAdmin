from PySide6.QtWidgets import QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QFormLayout
from app.view.screen import Screen


class CouponScreen(Screen):
    """ 쿠폰 관리 화면 (UI) """

    def __init__(self):
        super().__init__("쿠폰 관리")
        self.controller = None  # Controller 연결을 위한 변수

        # UI 구성에 사용될 멤버 변수
        self.coupon_list = None
        self.coupon_code_input = None
        self.coupon_expiration_input = None
        self.coupon_username_input = None
        self.coupon_usedAt_input = None
        self.coupon_used_input = None

        self.add_button = None
        self.save_button = None
        self.delete_button = None

        self.setup_ui()

    def set_controller(self, controller):
        self.controller = controller

    def setup_ui(self):
        """ UI 설정 """
        self.clear_screen()
        main_layout = QHBoxLayout()
        self.screen_layout.addLayout(main_layout)

        # 좌측: 쿠폰 리스트
        self.coupon_list = QListWidget()
        self.coupon_list.itemClicked.connect(lambda item: self.load_coupon(item))
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("쿠폰 목록"))
        left_layout.addWidget(self.coupon_list)

        # 우측: 쿠폰 추가/수정 UI (폼 구성)
        right_layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.coupon_code_input = QLineEdit()
        self.coupon_expiration_input = QLineEdit()
        self.coupon_username_input = QLineEdit()
        self.coupon_usedAt_input = QLineEdit()
        self.coupon_used_input = QLineEdit()

        # 필요에 따라 사용자가 직접 편집하지 못하도록 readOnly 설정 가능
        self.coupon_username_input.setReadOnly(True)
        self.coupon_usedAt_input.setReadOnly(True)
        self.coupon_used_input.setReadOnly(True)

        form_layout.addRow("쿠폰 코드:", self.coupon_code_input)
        form_layout.addRow("만료일:", self.coupon_expiration_input)
        form_layout.addRow("사용자:", self.coupon_username_input)
        form_layout.addRow("사용일시:", self.coupon_usedAt_input)
        form_layout.addRow("사용 여부:", self.coupon_used_input)

        # 버튼 추가
        self.add_button = QPushButton("새 쿠폰 추가")
        self.save_button = QPushButton("수정 내용 저장")
        self.delete_button = QPushButton("쿠폰 삭제")

        # 버튼 이벤트 연결
        self.add_button.clicked.connect(self.handle_add_coupon)
        self.save_button.clicked.connect(self.handle_update_coupon)
        self.delete_button.clicked.connect(self.handle_delete_coupon)

        right_layout.addWidget(QLabel("쿠폰 정보"))
        right_layout.addLayout(form_layout)
        right_layout.addWidget(self.add_button)
        right_layout.addWidget(self.save_button)
        right_layout.addWidget(self.delete_button)

        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 2)

    def display_coupons(self, coupons):
        """ 쿠폰 데이터를 리스트에 표시 (여기서는 'code' 필드를 사용) """
        self.coupon_list.clear()
        for coupon in coupons:
            # 리스트 항목에 코드와 선택적으로 username을 표시할 수 있음
            text = coupon.get("code", "")
            if coupon.get("username"):
                text += f" ({coupon['username']})"
            self.coupon_list.addItem(text)

    def load_coupon(self, item):
        """ 선택한 쿠폰 정보를 우측 패널에 로드 """
        selected_index = self.coupon_list.row(item)
        if self.controller:
            coupon_data = self.controller.get_coupon(selected_index)
            if coupon_data:
                # 각 필드를 설정 (None이면 빈 문자열로 처리)
                self.coupon_code_input.setText(coupon_data.get("code") or "")
                self.coupon_expiration_input.setText(coupon_data.get("expirationDate") or "")
                self.coupon_username_input.setText(coupon_data.get("username") or "")
                self.coupon_usedAt_input.setText(coupon_data.get("usedAt") or "")
                # used는 boolean일 경우, True/False를 문자열로 변환하여 표시
                used = coupon_data.get("used")
                self.coupon_used_input.setText(str(used) if used is not None else "")
            else:
                self.coupon_code_input.clear()
                self.coupon_expiration_input.clear()
                self.coupon_username_input.clear()
                self.coupon_usedAt_input.clear()
                self.coupon_used_input.clear()

    def handle_add_coupon(self):
        if self.controller:
            # add_coupon 호출 시, 필요한 정보만 전달 (여기서는 코드와 만료일)
            self.controller.add_coupon(
                self.coupon_code_input.text(),
                self.coupon_expiration_input.text()
            )

    def handle_update_coupon(self):
        if self.controller:
            index = self.coupon_list.currentRow()
            self.controller.update_coupon(
                index,
                self.coupon_code_input.text(),
                self.coupon_expiration_input.text()
            )

    def handle_delete_coupon(self):
        if self.controller:
            index = self.coupon_list.currentRow()
            if index >= 0:
                self.controller.delete_coupon(index, self.coupon_code_input.text())
