class CouponController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def load_coupons(self):
        # model.load_coupons()가 API 호출을 통해 최신 데이터를 반환한다고 가정
        self.view.display_coupons(self.model.load_coupons())

    def get_coupon(self, index):
        return self.model.get_coupon(index)

    def add_coupon(self, code, expiration_date):
        self.model.add_coupon(code, expiration_date)
        self.load_coupons()

    def update_coupon(self, index, code, expiration_date):
        self.model.update_coupon(index, code, expiration_date)
        self.load_coupons()

    def delete_coupon(self, index, code):
        self.model.delete_coupon(index, code)
        self.load_coupons()
