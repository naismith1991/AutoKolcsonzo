from Classes.Auto import Auto


class TeherAuto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras, loero):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras
        self.loero = loero

    @property
    def rendszam(self):
        return self._rendszam

    @property
    def tipus(self):
        return self._tipus

    @property
    def berleti_dij(self):
        return self._berleti_dij

    def berles(self):
        if not self._foglalt:
            self._foglalt = True
        else:
            print("Ez a kocsi már foglalt!")

    def berles_lemondas(self):
        if self._foglalt:
            self._foglalt = False
        else:
            print("Ez a kocsi nem volt foglalt!")