from Classes.Auto import Auto


class Berles:
    def __init__(self, auto: Auto, datum):
        self.auto = auto
        self.datum = datum

    def berles(self):
        return f'Bérlés: {self.auto.tipus} - {self.datum} '