# app/service/coupon_service.py
from app.service.api_client import APIClient


class CouponService:
    def __init__(self, api_client: APIClient = None):
        self.api_client = api_client or APIClient()

    def get_coupons(self):
        return self.api_client.get("/coupon")

    def add_coupon(self, code, date):
        payload = {"couponCode": code, "expirationDate": date}
        return self.api_client.post("/coupon", data=payload)

    def update_coupon(self, code, date):
        payload = {"couponCode": code, "expirationDate": date}
        return self.api_client.put(f"/coupon/{code}", data=payload)

    def delete_coupon(self, code):
        return self.api_client.delete(f"/coupon/{code}")
