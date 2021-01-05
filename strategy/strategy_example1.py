from abc import abstractmethod, ABC  # Python's built-in abstract class library

"""
https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e
"""


class IQuackStrategyAbstract(ABC):
    """Quack Strategy Interface."""

    @abstractmethod
    def quack(self) -> None:
        """Required Method."""
        pass


class LoudQuackStrategy(IQuackStrategyAbstract):
    """Loud quack."""
    def quack(self) -> None:
        print("QUACK! QUACK!!")


class GentleQuackStrategy(IQuackStrategyAbstract):
    """Normal quack."""
    def quack(self) -> None:
        print("quack!")


class ILightStrategyAbstract(ABC):
    """Light Strategy Interface."""

    @abstractmethod
    def lights_on(self) -> None:
        """Required Method."""
        pass


class OnForTenSecondsStrategy(ILightStrategyAbstract):
    """Lights on."""
    def lights_on(self) -> None:
        print("Lights on for 10 seconds")


loud_quack = LoudQuackStrategy()
gentle_quack = GentleQuackStrategy()
ten_seconds = OnForTenSecondsStrategy()


class Duck(object):
    """The Duck class."""
    def __init__(self, quack_strategy, light_strategy):
        self._quack_strategy = quack_strategy
        self._light_strategy = light_strategy

    def quack(self) -> None:
        self._quack_strategy.quack()

    def lights_on(self) -> None:
        self._light_strategy.lights_on()


# Types of Ducks
class VillageDuck(Duck):
    """Specific duck class."""
    def __init__(self):
        super(VillageDuck, self).__init__(loud_quack, None)

    @staticmethod
    def go_home() -> None:
        print("Going to the river")


class ToyDuck(Duck):
    """Specific duck class."""
    def __init__(self):
        super(ToyDuck, self).__init__(gentle_quack, ten_seconds)


class CityDuck(Duck):
    """Specific duck class."""
    def __init__(self):
        super(CityDuck, self).__init__(gentle_quack, None)

    @staticmethod
    def go_home() -> None:
        print("Going to the Central Park pond")


class RobotDuck(Duck):
    """Specific duck class."""
    def __init__(self):
        super(RobotDuck, self).__init__(loud_quack, ten_seconds)


# Note: Calling lights_on() on CityDuck or VillageDuck will result in AttributeError
robo = RobotDuck()
robo.quack()  # QUACK! QUACK!!
robo.lights_on()  # Lights on for 10 seconds

city = CityDuck()
city.quack()
city.go_home()
