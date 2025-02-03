from app.controller.coupon_controller import CouponController
from app.model.coupon_model import CouponModel
from app.view import *


class ScreenFactory:
    @classmethod
    def create_screen(cls, name):
        # 쿠폰 화면의 경우, 컨트롤러와 모델을 함께 생성하여 연결한다.
        if name == "쿠폰":
            screen = CouponScreen()
            model = CouponModel()
            controller = CouponController(model, screen)
            screen.set_controller(controller)
            return screen

        # 다른 화면들도 컨트롤러/모델이 필요한 경우 이와 유사하게 처리할 수 있음.
        # 예를 들어, "유저" 화면이 별도의 로직이 필요하다면:
        elif name == "유저":
            # 예: user 모델, user 컨트롤러를 생성 후 연결 (여기서는 단순히 뷰만 반환)
            return UserScreen()
        elif name == "체험단":
            return ExperienceScreen()
        elif name == "커뮤니티":
            return CommunityScreen()
        elif name == "설문":
            return SurveyScreen()
        elif name == "신고":
            return ReportScreen()
        else:
            raise ValueError(f"알 수 없는 화면 타입: {name}")
