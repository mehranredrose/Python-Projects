from samples import create_samples
from advertisment import ApartmentRent, ApartmentSale, HouseRent, HouseSale, StoreRent, StoreSale


class Handler:
    ADVERTISEMENT_TYPE = {
        1: ApartmentRent, 2: ApartmentSale,
        3: HouseRent, 4: HouseSale,
        5: StoreRent, 6: StoreSale
    }

    SWITCHES = {
        'r': 'get_report',
        's': 'show_all'
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPE:
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            print(adv, adv.manager.count())
            for obj in adv.object_list:
                print(obj.show_details)

    def run(self):
        for key in self.SWITCHES:
            print(f'press {key} for {self.SWITCHES[key]}')
        user_input = input('Enter Your Choice: ')
        switch = self.SWITCHES.get(user_input, None)

        if switch is None:
            print('Invalid Input!')
            self.run()

        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == "__main__":
    create_samples()
    handler = Handler().run()
