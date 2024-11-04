from Classes.Auto import Auto


class SzemelyAuto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ules_szam, loero):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ules_szam = ules_szam
        self._loero = loero

    @property
    def ules_szam(self):
        return self._ules_szam

    @ules_szam.setter
    def ules_szam(self, value):
        self._ules_szam = value

    @property
    def loero(self):
        return self._loero