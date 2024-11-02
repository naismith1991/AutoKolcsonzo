from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij
        self._foglalt = False

    @abstractmethod
    def berles(self):
        if not self._foglalt:
            self._foglalt = True
        else:
            print("Ez a kocsi már foglalt!")

    @abstractmethod
    def berles_lemondas(self):
        if self._foglalt:
            self._foglalt = False
        else:
            print("Ez a kocsi nem volt foglalt!")