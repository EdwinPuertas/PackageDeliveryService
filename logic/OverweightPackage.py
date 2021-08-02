from logic.Package import Package
from logic.Person import Person
from logic.Address import Address

class OverweightPackage(Package):

    def __init__(self, code: int = 0, weight: float = 0, cost: float = 0, description: str = "Descripcion",
                       sender: Person = None, receiver: Person = None, add_sender: Address = None,
                       add_receiver: Address = None, over_weight: float = 0, default_value: float = 0):
        super().__init__(code, weight, cost, description, sender, receiver, add_sender, add_receiver)
        self._over_weight = over_weight
        self._default_value = default_value

    @property
    def over_weight(self):
        return self._over_weight

    @over_weight.setter
    def over_weight(self, over_weight: float):
        self._over_weight = over_weight

    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: float):
        self._default_value = default_value

    def calculate(self):
        return super().calculate()+self.over_weight*(super().weight-75)+self.default_value

    def __str__(self):
        return super(OverweightPackage, self).__str__()+ '\nCosto Sobre Peso por gramo: {0}'.format(self.over_weight)


if __name__ == '__main__':
    from logic.Person import Person
    from logic.Address import Address

    ow=OverweightPackage()
    print(ow)