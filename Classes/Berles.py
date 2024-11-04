from xmlrpc.client import DateTime

from Classes.Auto import Auto


class Berles:
    def __init__(self, auto: Auto, datum):
        self._auto = auto
        self._datum = datum

    @property
    def auto(self):
        return self._auto

    @property
    def datum(self):
        return self._datum