class AutoKolcsonzo:
    def __init__(self, name):
        self._name = name
        self._autok = []

    @property
    def name(self):
        return self._name

    @property
    def autok(self):
        for auto in self._autok:
            print(f"Típus: {auto.tipus}, Bérleti díja: {auto.berleti_dij}, Rendszám: {auto.rendszam}")

    @autok.setter
    def autok(self, uj_auto):
        self._autok.append(uj_auto)

    def foglalas_rendszam_alapjan(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == auto_rendszam:
                return autok()