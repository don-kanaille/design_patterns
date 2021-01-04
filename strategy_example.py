from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Duck:
    def __init__(self, strategy: IQuackBehaviour) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> IQuackBehaviour:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: IQuackBehaviour) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Client delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        print("Client:")
        result = self._strategy.quack()


class IQuackBehaviour(ABC):

    @abstractmethod
    def quack(self) -> None:
        pass


class IFlyBehaviour(ABC):

    @abstractmethod
    def fly(self) -> None:
        pass


class IDisplayBehaviour(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayAsTextStrategy(IDisplayBehaviour):

    # concrete stratge
    def display(self) -> None:
        print("*text*")


class DisplayAsGraphicsStrategy(IDisplayBehaviour):
    def display(self) -> None:
        print("*graphic*")


class SimpleFlyStrategy(IFlyBehaviour):
    def fly(self) -> None:
        print("*flatter...flatter*")


class JetFlyStrategy(IFlyBehaviour):
    def fly(self) -> None:
        print("*zischhhhhhh*")


class NoFlyStrategy(IFlyBehaviour):
    def fly(self) -> None:
        print("*zirp*")


class SimpleQuackStrategy(IQuackBehaviour):
    def quack(self) -> None:
        print("Quack")


class NoQuackStrategy(IQuackBehaviour):
    def quack(self) -> None:
        print("*zirp...zirp*")


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    city_duck = Duck(SimpleQuackStrategy())
    print("Duck: Strategy is set to simple quack.")
    city_duck.do_some_business_logic()
    print()

    print("Duck: Strategy is set to no quack.")
    city_duck.strategy = NoQuackStrategy()
    city_duck.do_some_business_logic()
