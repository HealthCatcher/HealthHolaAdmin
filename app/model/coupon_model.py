from app.service.coupon_service import CouponService


class CouponModel:
    def __init__(self, coupon_service: CouponService = None):
        self.coupon_service = coupon_service or CouponService()
        self.coupons = []  # API를 통해 불러온 쿠폰 목록

    def load_coupons(self):
        # API를 통해 쿠폰 데이터를 가져와 self.coupons 업데이트
        self.coupons = self.coupon_service.get_coupons()
        return self.coupons

    def get_coupon(self, index):
        if 0 <= index < len(self.coupons):
            return self.coupons[index]
        return None

    def add_coupon(self, code, expiration_date):
        # coupon_service의 add_coupon 호출 (API의 요청 형식에 맞게 인자 수정)
        self.coupon_service.add_coupon(code, expiration_date)
        new_coupon = {"code": code, "expirationDate": expiration_date}
        self.coupons.append(new_coupon)
        return new_coupon

    def update_coupon(self, index, code, expiration_date):
        if 0 <= index < len(self.coupons):
            coupon = self.coupons[index]
            updated_coupon = self.coupon_service.update_coupon(code, expiration_date)
            self.coupons[index] = updated_coupon
            return updated_coupon
        return None

    def delete_coupon(self, index, code):
        if 0 <= index < len(self.coupons):
            coupon = self.coupons[index]
            self.coupon_service.delete_coupon(code)
            del self.coupons[index]
