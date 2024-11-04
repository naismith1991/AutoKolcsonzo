from datetime import datetime
from typing import List

from Classes.Berles import Berles


class Kolcsonzo:
    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek= []

    @property
    def nev(self):
        return self._nev

    @property
    def autok(self):
        return self._autok

    @autok.setter
    def auto_hozzaadasa(self, uj_auto):
        self.autok.append(uj_auto)

    @property
    def berlesek(self):
        return self._berlesek

    def autok_listazasa(self):
        for auto in self.autok:
            print(f"Autó típusa: {auto.tipus}, Bérleti díj: {auto.berleti_dij} Ft/nap, Rendszám: {auto.rendszam}")


    def berles_letrehozasa(self, rendszam, datum):
        if datum < datetime.today():
            print("Rossz dátumot adtál meg (korábbi a mai napnál).")
            return 0

        for auto in self._autok:
            if auto.rendszam == rendszam:
                for berles in self._berlesek:
                    if berles.auto.rendszam == rendszam and berles.datum == datum:
                        print("Ezt az autót már lefoglalták erre a megadott dátumra")
                        return 0

                berles = Berles(auto, datum)
                self._berlesek.append(berles)
                print(f"Sikeres bérlés! {berles.auto.tipus} - {berles.datum} napra - {berles.auto.berleti_dij} Ft/nap")
                return berles.auto.berleti_dij

        print("Nem megfelelő rendszámot adtál meg!")

    def berlesek_listazasa(self):
        if not self._berlesek:
            print("Nincs aktív bérlés.")
        for berles in self._berlesek:
            print(f"Bérlés: Típus: {berles.auto.tipus} Rendszáma: {berles.auto.rendszam} - Dátum: {berles.datum}")

    def berles_lemondasa(self, rendszam, datum):
        for berles in self._berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self._berlesek.remove(berles)
                print("A bérlés le lett mondva.")
                return
        print("Nincs ilyen bérlés.")

    def _auto_kereses(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                return auto
            print("Nem megfelelő rendszámot adtál meg!")

