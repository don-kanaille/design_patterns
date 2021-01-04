from abc import abstractmethod, ABCMeta  # Python's built-in abstract class library

"""
https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e
"""


class QuackStrategyAbstract(object):
    """
    abstract base class AKA ABC

    Abstract base classes complement duck-typing by providing a way to define interfaces.
    ABCs introduce virtual subclasses, which are classes that don’t inherit from a
    class but are still recognized by isinstance() and issubclass().
    """
    __metaclass__ = ABCMeta
    """
    ABCMeta = Metaclass for defining Abstract Base Classes (ABCs).
    
    Use this metaclass to create an ABC.
    An ABC can be subclassed directly, and then acts as a mix-in class.
    You can also register unrelated concrete classes (even built-in classes)
    and unrelated ABCs as “virtual subclasses”
    """

    @abstractmethod
    def quack(self):
        """Required Method"""


class LoudQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("QUACK! QUACK!!")


class GentleQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("quack!")


class LightStrategyAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def lights_on(self):
        """Required Method"""


class OnForTenSecondsStrategy(LightStrategyAbstract):
    def lights_on(self):
        print("Lights on for 10 seconds")


loud_quack = LoudQuackStrategy()
gentle_quack = GentleQuackStrategy()
ten_seconds = OnForTenSecondsStrategy()


class Duck(object):
    def __init__(self, quack_strategy, light_strategy):
        self._quack_strategy = quack_strategy
        self._light_strategy = light_strategy

    def quack(self):
        self._quack_strategy.quack()

    def lights_on(self):
        self._light_strategy.lights_on()


# Types of Ducks
class VillageDuck(Duck):
    def __init__(self):
        super(VillageDuck, self).__init__(loud_quack, None)

    def go_home(self):
        print("Going to the river")


class ToyDuck(Duck):
    def __init__(self):
        super(ToyDuck, self).__init__(gentle_quack, ten_seconds)


class CityDuck(Duck):
    def __init__(self):
        super(CityDuck, self).__init__(gentle_quack, None)

    def go_home(self):
        print("Going to the Central Park pond")


class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self).__init__(loud_quack, ten_seconds)


# Note: Calling lights_on() on CityDuck or VillageDuck will result in AttributeError
robo = RobotDuck()

robo.quack()  # QUACK! QUACK!!
robo.lights_on()  # Lights on for 10 seconds
