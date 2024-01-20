from base import BaseClass
from abc import abstractmethod


class EstateAbstract(BaseClass):
    def __init__(self, user, area, rooms_count, build_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.rooms_count = rooms_count
        self.build_year = build_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass


class Apartment(EstateAbstract):
    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f'Apartment : {self.id}')


class House(EstateAbstract):
    def __init__(self, has_yard, floor_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floor_count = floor_count
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f'House : {self.id}')


class Store(EstateAbstract):

    def show_description(self):
        print(f'Store : {self.id}')
