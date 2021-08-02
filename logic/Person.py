class Person(object):

    def __init__(self, id: int = 0, name: str = "Name", last_name: str = "LastName"):
        self._id = id
        self._name = name
        self._last_name = last_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name


    def __str__(self):
        return '{0}, {1}, {2}'.format(self.id, self.name, self.last_name)


if __name__ == '__main__':
    p1 = Person(id= 1010, name="Daniela", last_name="Franco")
    p2 = Person(id= 1234, name="Laura", last_name="Zambrano")
    print(p1)
    print(p2)