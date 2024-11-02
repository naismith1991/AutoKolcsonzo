from Classes.SzemelyAuto import SzemelyAuto
from Classes.TeherAuto import TeherAuto
from Classes.Kolcsonzo import Kolcsonzo

class FoglaloRendszer:

    def __init__(self):
        self._kolcsonzo = Kolcsonzo("Hertz")
        self._init_data()

    def _init_data(self):
        self._kolcsonzo.autok_hozzaadasa = SzemelyAuto("AAA-111", "Nissan Leaf", 15000, 4, 120)
        self._kolcsonzo.autok_hozzaadasa = SzemelyAuto("BBB-222", "Toyota Yaris", 10000, 5, 150)
        self._kolcsonzo.autok_hozzaadasa = SzemelyAuto("CCC-333", "Mazda 6", 20000, 5, 180)
        self._kolcsonzo.autok_hozzaadasa = TeherAuto("AE-CC-008", "Fiat Iveco", 40000, 2000, 300)

    def user_interact(self):
        while True:
            print("1 - Autók listázása")
            print("2 - Autó bérlése")
            print("3 - Bérlés lemondása")
            print("4 - Bérlések listázása")
            print("5 - Kilépés")

            choice = input("Válasz a fenti menüpontok közül: ")

            if choice == "1":
                self._kolcsonzo.autok_listazasa
            elif choice == "2":
                rendszam = input("Add meg a rendszámát a kocsinak, amit szeretnél lefoglalni!")
                self._kolcsonzo.foglalas_rendszam(rendszam)
            elif choice == "3":
                rendszam = input("Add meg a rendszámát a kocsinak, amit le szeretnél mondani!")
                self._kolcsonzo.lemondas_rendszam(rendszam)
            elif choice == "4":
                break

foglaloRendszer = FoglaloRendszer()
foglaloRendszer.user_interact()