from logic.Package import Package
from logic.StandardPackage import StandardPackage
from logic.OverweightPackage import OverweightPackage
from logic.Person import Person
from logic.Address import Address

if __name__ == '__main__':
    code = int(input("Ingrese el código: "))
    description = str(input("Ingrese la descripción del artículo a enviar: "))
    weight = float(input("Ingrese el peso del paquete en gramos: "))
    p1 = Person(name="Daniela", last_name="Franco")
    p2 = Person(name="Laura", last_name="Zambrano")
    d1 = Address(city="Bogotá", state="Cundinamarca", country="Colombia", street="Calle 26", number=1227,
                 postal=112232, floor=3, apartment=301)
    d2 = Address(city="Bogotá", state="Cundinamarca", country="Colombia",street="Carrera 23", number=12253,
                 postal=111000, floor=4, apartment=402)

    if weight > 0 and weight <= 75:
        default_value = 5000
        cost = 100
        standard_package = StandardPackage(code=code, weight=weight, cost=cost, description=description,
                                           default_value=default_value, sender = p1, receiver = p2, add_sender = d1,
                                           add_receiver = d2)
        print(standard_package)
        print(StandardPackage.calculate(standard_package))
        print("Paquete Estándard")

    elif weight > 75:
        default_value = 5000
        over_weight = 150
        cost = 100
        over_weight_package = OverweightPackage(code=code, weight=weight, cost=cost, description=description,
                                                over_weight=over_weight, default_value=default_value, sender = p1,
                                                receiver = p2, add_sender = d1, add_receiver = d2)
        print(over_weight_package)
        print(OverweightPackage.calculate(over_weight_package))
        print("Paquete con sobrepeso")

    else:
        print("Vuelva a ingresar la información")
