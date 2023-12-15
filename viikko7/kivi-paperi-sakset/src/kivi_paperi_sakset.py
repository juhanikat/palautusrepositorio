from tuomari import Tuomari


class KiviPaperiSakset:

    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            if not self._onko_ok_siirto(ekan_siirto):
                break
            tokan_siirto = self._toisen_siirto()
            if not self._onko_ok_siirto(tokan_siirto):
                break
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
