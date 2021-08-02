from logic.Person import Person
from logic.Address import Address

class Package(object):

    def __init__(self, code: int = 0, weight: float = 0, cost: float = 0, description: str = "Descripcion",
                 id_sender: Person = None, sender: Person = None, id_receiver: Person = None, receiver: Person = None,
                 add_sender: Address = None, add_receiver: Address = None):
        self.code = code
        self.weight = weight
        self.cost = cost
        self.description = description
        self.id_sender = id_sender
        self.sender = sender
        self.id_receiver = id_receiver
        self.receiver = receiver
        self.add_sender = add_sender
        self.add_receiver = add_receiver

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code: int):
        self._code = code

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        self._weight = weight

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost: float):
        self._cost = cost

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def id_sender(self):
        return self._id_sender

    @id_sender.setter
    def id_sender(self, id_sender: Person):
        self._id_sender = id_sender

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender: Person):
        self._sender = sender

    @property
    def id_receiver(self):
        return self._id_receiver

    @id_receiver.setter
    def id_receiver(self, id_receiver: Person):
        self._id_receiver = id_receiver

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: Person):
        self._receiver = receiver

    @property
    def add_sender(self):
        return self._add_sender

    @add_sender.setter
    def add_sender(self, add_sender: Address):
        self._add_sender = add_sender

    @property
    def add_receiver(self):
        return self._add_receiver

    @add_receiver.setter
    def add_receiver(self, add_receiver: Address):
        self._add_receiver = add_receiver

    def calculate(self):
        return self.weight*self.cost

    def __str__(self):
        return 'Paquete: Código: {0}\nPeso(gr):{1}\nCosto por gramo sin sobrepeso:{2}\nDescripción:{3}\nRemitente: {4}\nReceptor: {5}' \
               '\nDirección remitente: {6}\nDirección receptor: {7}\nCosto Total: {8}'.format(self.code, self.weight,
                                                                                           self.cost, self.description,
                                                                                           self.sender, self.receiver,
                                                                                           self.add_sender,
                                                                                           self.add_receiver,
                                                                                           self.calculate())


if __name__ == '__main__':
    from logic.Person import Person
    from logic.Address import Address

    p1 = Person(id= 1010, name="Daniela", last_name="Franco")
    p2 = Person(id=1234, name="Laura", last_name="Zambrano")
    d1 = Address(city="Bogotá", state="Cundinamarca", country="Colombia", street="Calle 26",
                 postal=112232, floor=3, apartment=301)
    d2 = Address(city="Bogotá", state="Cundinamarca", country="Colombia",street="Carrera 23",
                 postal=111000, floor=4, apartment=402)
    package1 = Package(code=000, weight=125.3, cost=500, description="Paquete delicado", sender=p1, receiver=p2,
                       add_sender=d1, add_receiver=d2)

    print(package1)