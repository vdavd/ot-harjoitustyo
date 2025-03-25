import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_arvo_alussa_okein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15)

    def test_saldo_vahenee_oikein_rahaa_ottaessa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5)

    def test_saldo_ei_mene_miinukselle(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_ota_rahaa_palauttaa_oikean_totuusarvon(self):
        failure = self.maksukortti.ota_rahaa(1500)
        self.assertEqual(failure, False)

        success = self.maksukortti.ota_rahaa(500)
        self.assertEqual(success, True)

    def test_str_palauttaa_oikean_merkkijonon(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
