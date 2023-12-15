from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self, parempi=False) -> None:
        super().__init__()
        if parempi:
            self.tekoaly = TekoalyParannettu()
        else:
            self.tekoaly = Tekoaly()

    def _toisen_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tekoälyn siirto: {siirto}")
        return siirto
