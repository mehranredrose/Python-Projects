from estate import Apartment, House, Store
from deal import Sale, Rent
from base import BaseClass


class ApartmentSale(BaseClass, Apartment, Sale):
    def show_details(self):
        self.show_description()
        self.show_price()


class ApartmentRent(BaseClass, Apartment, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseSale(BaseClass, House, Sale):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseRent(BaseClass, House, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreSale(BaseClass, Store, Sale):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreRent(BaseClass, Store, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()
