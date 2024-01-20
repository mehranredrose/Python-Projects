from samples import create_samples
from advertisment import ApartmentRent, ApartmentSale, HouseRent, HouseSale, StoreRent, StoreSale


class Handler:

    def run(self):
        pass


if __name__ == "__main__":
    create_samples()
    handler = Handler()

    handler.run()
