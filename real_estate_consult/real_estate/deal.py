from base import BaseClass


class Sale(BaseClass):
    def __init__(self, price_per_meter, discount, convert, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discount = discount
        self.convert = convert
        super().__init__(*args, **kwargs)


class Rent(BaseClass):
    def __init__(self, initial_price, monthly_price, convert, discount, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convert = convert
        self.discount = discount
        super().__init__(*args, **kwargs)
