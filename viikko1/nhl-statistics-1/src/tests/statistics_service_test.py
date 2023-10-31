import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_pelaajan_etsiminen_toimii(self):
        pelaaja = self.stats.search("Semenko")
        self.assertIsInstance(pelaaja, Player)
        pelaaja = self.stats.search("random")
        self.assertAlmostEqual(pelaaja, None)
    
    def test_joukkueen_pelaajien_listaaminen(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)
    
    def test_parhaimmat_pelaajat(self):
        parhaat = self.stats.top(2)
        self.assertEqual(parhaat[0].name, "Gretzky")
        self.assertEqual(parhaat[1].name, "Lemieux")

    def test_parhaimmat_pelaajat_maaleissa(self):
        parhaat = self.stats.top(2, sorted_by=SortBy.GOALS)
        self.assertEqual(parhaat[0].name, "Lemieux")
        self.assertEqual(parhaat[1].name, "Yzerman")
    
    def test_parhaimmat_pelaajat_assisteissa(self):
        parhaat = self.stats.top(2, sorted_by=SortBy.ASSISTS)
        self.assertEqual(parhaat[0].name, "Gretzky")
        self.assertEqual(parhaat[1].name, "Yzerman")
        
        
        
