from Classes.Auto import Auto


class TeherAuto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras, loero):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras
        self._loero = loero

    @property
    def teherbiras(self):
        return self._teherbiras

    @property
    def loero(self):
        return self._loero