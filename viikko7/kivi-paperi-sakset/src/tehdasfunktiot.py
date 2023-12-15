from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


class TehdasFunktiot:

    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_tekoaly_peli():
        return KPSTekoaly()

    @staticmethod
    def luo_parempi_tekoaly_peli():
        return KPSTekoaly("parempi")
