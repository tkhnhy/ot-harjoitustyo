import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_maksukorttille_latautuu_raha(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_maksukortti_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 500)
    
    def test_maksukortti_saldo_ei_vahene_jos_liikaa(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_maksukortti_ota_rahaa_metodi_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_maksukortti_ota_rahaa_metodi_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_saldo_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
    
    def test_str_oikea(self):
        palaute = "Kortilla on rahaa {:0.2f} euroa".format(round(self.maksukortti.saldo / 100, 2))

        self.assertEqual(self.maksukortti.__str__(), palaute)