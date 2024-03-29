from base import BaseClass


class User(BaseClass):
    def __init__(self, first_name, last_name, contact, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        super().__init__(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
