
class Kolcsonzo:
    def __init__(self, name):
        self._name = name
        self._autok = []

    @property
    def name(self):
        return self._name

    @property
    def autok_listazasa(self):
        for auto in self._autok:
            print(f"Típus: {auto.tipus}, Bérleti díja: {auto.berleti_dij} Ft/nap, Rendszám: {auto.rendszam}")

    @autok_listazasa.setter
    def autok_hozzaadasa(self, uj_auto):
        self._autok.append(uj_auto)

    def foglalas_rendszam(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                auto.berles()

    def lemondas_rendszam(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                auto.berles_lemondas()

