from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IObserver(ABC):
    """Interface Observable."""

    @abstractmethod
    def update(self, subject: IObservable) -> None:
        pass


class IObservable(ABC):
    """Interface Observer."""

    @abstractmethod
    def add_(self, observer: IObserver) -> None:
        """Adds an observer."""
        pass

    @abstractmethod
    def remove_(self, observer: IObserver) -> None:
        """Remove an observer."""
        pass

    @abstractmethod
    def notify_(self) -> None:
        """Notify all added observers."""
        pass


class Weatherstation(IObservable):
    """Observable."""

    # Initial State
    _state: int = None
    # List of observers
    _observers: List[IObserver] = []

    def add_(self, observer: IObserver) -> None:
        self._observers.append(observer)
        print("Add observer: {}".format(str(observer)))

    def remove_(self, observer: IObserver) -> None:
        self._observers.remove(observer)
        print("Remove observer: {}".format(str(observer)))

    def notify_(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update_(self)

    def get_temperature(self) -> float:
        return 0.0


class Phone1(IObserver):
    """Observer."""
    def update_(self, observer: IObservable) -> None:
        print("Updating...")


class Phone2(IObserver):
    """Observer."""
    def update_(self, observer: IObservable) -> None:
        print("Updating...")


if __name__ == "__main__":
    pass
