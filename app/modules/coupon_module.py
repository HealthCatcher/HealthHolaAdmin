# app/modules/coupon_module.py
from app.model.coupon_model import CouponModel
from app.controller.coupon_controller import CouponController
from app.service.api_client import APIClient
from app.service.coupon_service import CouponService
from app.view.coupon_screen import CouponScreen


def create_coupon_module(api_client=None):
    api_client = api_client or APIClient()
    coupon_service = CouponService(api_client)
    coupon_model = CouponModel(coupon_service)
    coupon_view = CouponScreen()
    coupon_controller = CouponController(coupon_model, coupon_view)
    coupon_view.set_controller(coupon_controller)

    coupon_controller.load_coupons()

    return coupon_view
