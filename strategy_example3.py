from abc import abstractmethod, ABC


class IAngriffsArt(ABC):
    """Interface. Abstrakte Klasse"""
    @abstractmethod
    def ang(self):
        pass


class AngriffsArtFeuer(IAngriffsArt):
    """Konkrete Klasse."""
    def ang(self):
        print("Ich speihe Feuer!")


class AngriffsArtLaser(IAngriffsArt):
    """Konkrete Klasse."""
    def ang(self):
        print("Ich schieße Laser!")


class Monster:
    """Hauptklasse."""
    def __init__(self, angriffs_art):
        self.angriff = angriffs_art

    def laufen(self) -> None:
        print("Ich kann laufen!")

    def schwimmen(self) -> None:
        print("Ich kann schwimmen!!")

    def angreifen(self) -> None:
        self.angriff.ang()


laser = AngriffsArtLaser()
feuer = AngriffsArtFeuer()


class Zyklop(Monster):
    """Monster-Variation."""
    def __init__(self):
        super(Zyklop, self).__init__(laser)


class Drache(Monster):
    """Monster-Variation."""
    def __init__(self):
        super(Drache, self).__init__(feuer)


if __name__ == "__main__":
    zyklop = Zyklop()
    zyklop.laufen()
    zyklop.schwimmen()
    zyklop.angreifen()

    drache = Drache()
    drache.laufen()
    drache.schwimmen()
    drache.angreifen()
