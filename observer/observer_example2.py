from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IObserver(ABC):
    """Interface Observable."""
    def __init__(self, name: str):
        self.__name__ = name

    @abstractmethod
    def update_(self, subject: IObservable) -> None:
        pass


class IObservable(ABC):
    """Interface Observer."""
    def __init__(self, name: str):
        self.__name__ = name

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


class WeatherStation(IObservable):
    """Observable."""

    # Initial State
    _state: int = None
    # List of observers
    _observers: List[IObserver] = []

    def add_(self, observer: IObserver) -> None:
        self._observers.append(observer)
        print("Add observer: {}".format(observer.__name__))

    def remove_(self, observer: IObserver) -> None:
        self._observers.remove(observer)
        print("Remove observer: {}".format(observer.__name__))

    def notify_(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update_(self)

    @staticmethod
    def get_temperature() -> float:
        return 37.7


class IDisplay(ABC):
    """Display Interface."""

    @abstractmethod
    def display(self, device) -> None:
        pass


class Phone1(IObserver, IDisplay):
    """Observer."""
    def update_(self, observer: IObservable) -> None:
        print("Update: There was a change in Temperature in {}!".format(observer.__name__))
        self.display(observer)

    def display(self, device) -> None:
        print("Display: {}".format(device.__name__))


class Phone2(IObserver, IDisplay):
    """Observer."""
    def update_(self, observer: IObservable) -> None:
        print("Update: There was a change in Temperature in {}!".format(observer.__name__))
        self.display(observer)

    def display(self, device) -> None:
        print("Display: {}".format(device.__name__))


if __name__ == "__main__":
    weather_station = WeatherStation(name="weather_station")
    phone1 = Phone1(name="phone1")
    phone2 = Phone2(name="phone2")
    weather_station.add_(phone1)
    weather_station.add_(phone2)
    weather_station.notify_()
