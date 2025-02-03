from app.controller.coupon_controller import CouponController
from app.model.coupon_model import CouponModel
from app.view import CouponScreen

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    # Model, View, Controller 생성
    model = CouponModel()
    view = CouponScreen()
    controller = CouponController(model, view)

    # 초기 쿠폰 로드
    controller.load_coupons()

    view.show()
    sys.exit(app.exec())
