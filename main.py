from Classes.SzemelyAuto import SzemelyAuto
from Classes.TeherAuto import TeherAuto
from Classes.AutoKolcsonzo import AutoKolcsonzo

class FoglaloRendszer:

    def __init__(self):
        self._autoKolcsonzo = AutoKolcsonzo("Hertz")
        self._init_data()

    def _init_data(self):
        self._autoKolcsonzo.autok = SzemelyAuto("AAA-111", "Nissan Leaf", 15000)
        self._autoKolcsonzo.autok = SzemelyAuto("BBB-222", "Toyota Yaris", 10000)
        self._autoKolcsonzo.autok = SzemelyAuto("CCC-333", "Mazda 6", 20000)
        self._autoKolcsonzo.autok = TeherAuto("AE-CC-008", "Fiat Iveco", 40000)

    def user_interact(self):
        while True:
            print("1 - Autók listázása")
            print("2 - Autó bérlése")
            print("3 - Bérlés lemondása")
            print("4 - Bérlések listázása")
            print("5 - Kilépés")

            choice = input("Válasz a fenti menüpontok közül: ")

            if choice == "1":
                self._autoKolcsonzo.autok
            elif choice == "2":
                room = int(input("Add meg a rendszámát a kocsinak, amit szeretnél lefoglalni!"))
                self._autoKolcsonzo.book_by_room_number(room)
            elif choice == "3":
                room = int(input("Add meg a szoba számát, amit szeretnél lemondani!"))
                self._hotel.unbook_by_room_number(room)
            elif choice == "4":
                break