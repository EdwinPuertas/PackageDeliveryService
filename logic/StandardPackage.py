from logic.Package import Package
from logic.Person import Person
from logic.Address import Address

class StandardPackage(Package):

    def __init__(self, code: int = 0, weight: float = 0, cost: float = 0, description: str = "Descripcion",
                       sender: Person = None, receiver: Person = None, add_sender: Address = None,
                       add_receiver: Address = None, default_value: float = 0):
        super().__init__(code, weight, cost, description, sender, receiver, add_sender, add_receiver)
        self._default_value = default_value

    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: float):
        self._default_value = default_value

    def calculate(self):
        return super().calculate()+self.default_value

    def __str__(self):
        return super(StandardPackage, self).__str__()+ '\nCuota Fija: {0}'.format(self.default_value)


if __name__ == '__main__':
    from logic.Person import Person
    from logic.Address import Address

    sp=StandardPackage()
    print(sp)
