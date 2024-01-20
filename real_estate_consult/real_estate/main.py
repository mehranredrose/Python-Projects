from random import choice
from user import User
from region import Region
from estate import Apartment, House, Store


# creating some random Users
names = ['Josh', 'Joe', 'Jim']
last_names = ['fury', 'Johnson', 'Cross']
phones = ['09123456789', '09123459876',
          '09125436789', '09123459867', '09129873456']

for number in phones:
    User(choice(names), choice(last_names), number)

for user in User.object_list:
    pass
# now we have 5 users


#    creating some regions
#    a region has only name.

rgn1 = Region('Vali asr')
rgn2 = Region('Zaferaniyeh')
rgn3 = Region('Tajrish')


'''Creating some apartments:
    an apartment is a class that inherits from EstateAbstract
    so we have apartment args and EstateAbstract args.
    
    EstateAbstract args are :
        user, area, rooms_count, build_year, region, address
    
    Apartment args are:
        has_elevator, has_parking, floor
'''
apt1 = Apartment(user=User.object_list[0], area=80, room_count=2,
                 build_year=2016, region=rgn3, address='Tajrish', has_elevator=True, has_parking=False, floor=5)
apt3 = Apartment(User.object_list[1], area=300, room_count=5,
                 build_year=2020, region=rgn2, address='zaferaniye', has_elevator=True, has_parking=True, floor=7)
apt3 = Apartment(User.object_list[2], area=45, room_count=1,
                 build_year=2006, region=rgn1, address='ValiAsr', has_elevator=False, has_parking=True, floor=3)

# Creating House and Store
hse1 = House(has_yard=True, floor_count=2,
             user=User.object_list[4], area=80, room_count=2,
             build_year=2016, region=rgn3, address='Tajrish')

store1 = Store(user=User.object_list[5], area=50, room_count=1,
               build_year=2012, region=rgn3, address='Tajrish')


if __name__ == "__main__":
    pass
