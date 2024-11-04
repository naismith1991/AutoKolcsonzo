from datetime import datetime

from Classes.Berles import Berles
from Classes.SzemelyAuto import SzemelyAuto
from Classes.TeherAuto import TeherAuto
from Classes.Kolcsonzo import Kolcsonzo

class FoglaloRendszer:

    def __init__(self):
        self.kolcsonzo = Kolcsonzo("Hertz")
        self._init_data()

    def _init_data(self):
        auto1  = SzemelyAuto("AAA-111", "Nissan Leaf", 15000, 4, 120)
        auto2  = SzemelyAuto("BBB-222", "Toyota Yaris", 10000, 5, 150)
        auto3 = SzemelyAuto("CCC-333", "Mazda 6", 20000, 5, 180)
        auto4 = TeherAuto("DDD-444", "Fiat Iveco", 40000, 2000, 300)

        self.kolcsonzo.autok.append(auto1)
        self.kolcsonzo.autok.append(auto2)
        self.kolcsonzo.autok.append(auto3)
        self.kolcsonzo.autok.append(auto4)

        self.kolcsonzo.berlesek.append(Berles(auto1, datetime.strptime("2024-12-10", "%Y-%m-%d")))
        self.kolcsonzo.berlesek.append(Berles(auto1, datetime.strptime("2024-12-12", "%Y-%m-%d")))
        self.kolcsonzo.berlesek.append(Berles(auto2, datetime.strptime("2024-12-13", "%Y-%m-%d")))
        self.kolcsonzo.berlesek.append(Berles(auto3, datetime.strptime("2024-12-10", "%Y-%m-%d")))

    def user_interact(self):
        while True:
            print("1 - Autók listázása")
            print("2 - Autó bérlése")
            print("3 - Bérlések listázása")
            print("4 - Bérlések lemondása")
            print("5 - Kilépés")

            choice = input("Válasz a fenti menüpontok közül: ")

            if choice == "1":
                self.kolcsonzo.autok_listazasa()
            elif choice == "2":
                rendszam_input = input("Adja meg a bérelni kívánt kocsi rendszámát!")
                datum_input = input("Adja meg a bérlés dátmát (YYYY-MM-DD formétumban): ")
                try:
                    datum_input = datetime.strptime(datum_input, "%Y-%m-%d")
                    self.kolcsonzo.berles_letrehozasa(rendszam_input, datum_input)
                except ValueError:
                    print("Hibás dátumformátum! Használja a YYYY-MM-DD formátumot!")

            elif choice == "3":
                self.kolcsonzo.berlesek_listazasa()

            elif choice == "4":
                rendszam = input("Adja meg a rendszámot: ")
                datum = input("Adja meg a foglalás dátumát(YYYY-MM-DD): ")
                try:
                    datum = datetime.strptime(datum, "%Y-%m-%d")
                    self.kolcsonzo.berles_lemondasa(rendszam, datum)
                except ValueError:
                    print("Hibás dátumformátum! Használja a YYYY-MM-DD formátumot!")
            elif choice == "5":
                break
            else:
                print("Hibás választás")


foglaloRendszer = FoglaloRendszer()
foglaloRendszer.user_interact()