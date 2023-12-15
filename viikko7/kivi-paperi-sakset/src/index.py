from tehdasfunktiot import TehdasFunktiot


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus not in ['a', 'b', 'c']:
            break
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        if vastaus.endswith("a"):
            peli = TehdasFunktiot.luo_kaksinpeli()
        elif vastaus.endswith("b"):
            peli = TehdasFunktiot.luo_tekoaly_peli()
        elif vastaus.endswith("c"):
            peli = TehdasFunktiot.luo_parempi_tekoaly_peli()

        peli.pelaa()


if __name__ == "__main__":
    main()
