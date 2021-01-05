from __future__ import annotations


class Beverage:
    """Component"""

    def cost(self) -> float:
        pass


class Espresso(Beverage):
    """Concrete Component"""

    def cost(self) -> float:
        """Returns the cost of 1.0"""
        return 1.0


class AddonDecorator(Beverage):
    """Decorator"""

    # The Decorator is AND has a Beverage!!!
    _component: Beverage = None

    def __init__(self, component: Beverage) -> None:
        self._component = component

    @property
    def component(self) -> Beverage:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._component

    def cost(self) -> float:
        pass


class Caramel(AddonDecorator):
    """Concrete Decorator"""

    def cost(self) -> float:
        """Adds the cost of 2.0"""
        return self.component.cost() + 2.0


class Cream(AddonDecorator):
    """Concrete Decorator"""

    def cost(self) -> float:
        """Adds the cost of 4.0"""
        return self.component.cost() + 3.0


def client_code(component: Beverage) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    # ...

    print(f"RESULT: {component.cost()}", end="\n")

    # ...


if __name__ == "__main__":
    # Std espresso
    espresso = Espresso()
    print("Client: Now I've got a Espresso")
    client_code(espresso)

    # Espresso with Caramel
    espresso_with_caramel = Caramel(espresso)
    print("Client: Now I've got a Espresso with Caramel")
    client_code(espresso_with_caramel)

    # Espresso with Cream
    espresso_with_cream = Cream(espresso)
    print("Client: Now I've got a Espresso with Caramel")
    client_code(espresso_with_cream)

    # Espresso with Caramel & Cream
    espresso_with_caramel = Caramel(espresso)
    espresso_with_caramel_and_cream = Cream(espresso_with_caramel)
    print("Client: Now I've got a Espresso with Caramel & Caramel")
    client_code(espresso_with_caramel_and_cream)
