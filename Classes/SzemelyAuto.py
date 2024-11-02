from Auto import Auto


class SzemelyAuto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ules_szam, loero):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ules_szam = ules_szam
        self.loero = loero


    def auto_adatok(self):
        return(f'Auto adatai: Rendszám: {self.rendszam}, Típusa: {self.tipus}, Ülések száma: {self.ules_szam},'
              f'Lóerő= {self.loero}, Bérleti díja: {self.berleti_dij}')


    def berles_lemondas(self):
        pass

    def berles_listazas(self):
        pass

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
        else:
            print("Hiba, a szoba már foglalt!")

    def unbook_room(self):
        if self.is_booked:
            self.is_booked = False
        else:
            print("Hiba, a szoba nem is volt foglalt!")