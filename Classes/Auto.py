from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.szabad = True

    @abstractmethod
    def auto_adatok(self):
        pass

    @abstractmethod
    def berles(self):
        pass

    @abstractmethod
    def berles_lemondas(self):
        pass

    @abstractmethod
    def berles_listazas(self):
        pass