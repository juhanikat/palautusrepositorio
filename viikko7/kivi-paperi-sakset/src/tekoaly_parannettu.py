# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self):
        self._muisti = []

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        self._muisti.append(siirto)

    def anna_siirto(self):
        if len(self._muisti) in range(0, 2):
            self._muisti.append("k")
            return "k"

        viimeisin_siirto = self._muisti[-1]

        k = 0
        p = 0
        s = 0

        for i in range(0, len(self._muisti) - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]
                if seuraava == "k":
                    k += 1
                elif seuraava == "p":
                    p += 1
                else:
                    s += 1
        print(k, p, s)
        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        siirto = None
        if k > p and k > s:
            siirto = "p"
        elif p > k and p > s:
            siirto = "s"
        else:
            siirto = "k"

        self._muisti.append(siirto)
        return siirto

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
