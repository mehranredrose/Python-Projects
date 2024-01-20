from estate import Apartment, House, Store
from deal import Sale, Rent


class ApartmentSale(Apartment, Sale):
    def show_details(self):
        self.show_description()
        self.show_price()


class ApartmentRent(Apartment, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseSale(House, Sale):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseRent(House, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreSale(Store, Sale):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreRent(Store, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()
