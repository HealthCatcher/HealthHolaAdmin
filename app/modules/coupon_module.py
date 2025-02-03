# app/modules/coupon_module.py
from app.model.coupon_model import CouponModel
from app.controller.coupon_controller import CouponController
from app.view.coupon_screen import CouponScreen


def create_coupon_module():
    view = CouponScreen()
    model = CouponModel()
    controller = CouponController(model, view)
    view.set_controller(controller)
    controller.load_coupons()
    return view
