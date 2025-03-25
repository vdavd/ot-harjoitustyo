import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_arvot_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisella_maksu_kun_rahat_riittaa(self):
        vaihtoraha_edullinen = self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(vaihtoraha_edullinen, 160)

        vaihtoraha_maukas = self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1006.4)
        self.assertEqual(vaihtoraha_maukas, 200)

    def test_lounaiden_maara_kasvaa_kateisella_ostaessa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisella_maksu_kun_rahat_ei_riita(self):
        vaihtoraha_edullinen = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(vaihtoraha_edullinen, 200)

        vaihtoraha_maukas = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(vaihtoraha_maukas, 200)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_kun_rahat_riittaa(self):
        edullinen = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 7.60)
        self.assertEqual(edullinen, True)

        maukas = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 3.60)
        self.assertEqual(maukas, True)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_korttiosto_toimii_kun_rahat_ei_riita(self):
        kortti = Maksukortti(100)

        edullinen = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 1)
        self.assertEqual(edullinen, False)

        maukas = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(), 1)
        self.assertEqual(maukas, False)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kortille_rahan_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010)
        self.assertEqual(self.kortti.saldo_euroina(), 20)

    def test_kortille_ei_voi_ladata_0_tai_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 0)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kortti.saldo_euroina(), 10)

        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kortti.saldo_euroina(), 10)

    