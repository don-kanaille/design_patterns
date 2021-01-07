from __future__ import annotations
from abc import ABC, abstractmethod


class Animal(ABC):
    """Product."""


class Dog(Animal):
    """Concrete Product Dog."""


class Cat(Animal):
    """Concrete Product Cat."""


class Duck(Animal):
    """Concrete Product Duck."""


class AnimalFactory(ABC):
    """Creator."""

    @abstractmethod
    def animal_create(self) -> Animal:
        """Creates Animals."""
        pass


class RandomAnimalFactory(AnimalFactory):
    """Concrete (Random) Creator."""

    def animal_create(self) -> Animal:
        pass


class BalancedAnimalFactory(AnimalFactory):
    """Concrete (Balanced) Creator."""

    def animal_create(self) -> Animal:
        pass
