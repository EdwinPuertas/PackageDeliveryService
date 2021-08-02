class Address(object):

    def __init__(self, country: str = "Country", city: str = "City", street: str = "Street",
                 postal: int = 0, state: str = "State", floor: int = 0, apartment: int = 0):
        self._country = country
        self._city = city
        self._street = street
        self._postal = postal
        self._state = state
        self._floor = floor
        self._apartment = apartment

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country: str):
        self._country = country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street: str):
        self._street = street

    @property
    def postal(self):
        return self._postal

    @postal.setter
    def postal(self, postal: int):
        self._postal = postal

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, floor: int):
        self._floor = floor

    @property
    def apartment(self):
        return self._apartment

    @apartment.setter
    def apartment(self, apartment: int):
        self._apartment = apartment

    def __str__(self):
        return '{4}, {0}, {1}, {2}, {3}, {5}, {6}'.format(self.city, self.state, self.country, self.street,
                                                              self.postal, self.floor, self.apartment)


if __name__ == '__main__':
    d1 = Address(city="Bogotá", state="Cundinamarca", country="Colombia",
                 street="Calle 26 #11-12", postal=112232, floor=3, apartment=301)
    d2 = Address(city="Bogotá", state="Cundinamarca", country="Colombia",
                 street="Carrera 23 #122-53", postal=111000, floor=4, apartment=402)
    print(d1)
    print(d2)