from abc import ABC


class Sale(ABC):
    def __init__(self, price_per_meter, discount, convert, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discount = discount
        self.convert = convert
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(
            f'Price={self.price_per_meter} , Discount= {self.discount} , Convert= {self.convert}')


class Rent(ABC):
    def __init__(self, initial_price, monthly_price, convert, discount, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convert = convert
        self.discount = discount
        super().__init__(*args, **kwargs)
