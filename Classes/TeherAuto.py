from Auto import Auto


class TeherAuto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras, loero):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras
        self.loero = loero

    def auto_adatok(self):
        return (f'Teherautó adatai: Rendszám: {self.rendszam}, Típusa: {self.tipus},'
                f'Lóerő: {self.loero}, Teherbírás: {self.teherbiras}, Bérleti díja: {self.berleti_dij}')

    def berles(self):
        pass

    def berles_lemondas(self):
        pass

    def berles_listazas(self):
        pass