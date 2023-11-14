import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.koyhamaksukortti = Maksukortti(100)

    def test_kassassa_alkuraha(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    #Edulliset kateinen

    def test_kassassa_alku_edullisesti(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassassa_alku_maukkaasti(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_raha_nousee(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_syo_edulliesti_kateisella_maara_nousee(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_ei_riita_kassa_ei_muutu(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(180), 180)
    
    def test_syo_edullisesti_ei_riita_edulliset_maara(self):
        kassapaate = Kassapaate()
        kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(kassapaate.edulliset, 0)

    #Maukkaat kateinen

    def test_syo_maukkaasti_kateisella_raha_nousee(self):
        kassapaate = Kassapaate()
        kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

    def test_syo_maukkaasti_kateisella_maara_nousee(self):
        kassapaate = Kassapaate()
        kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_ei_riita_kassa_ei_muutu(self):
        kassapaate = Kassapaate()
        kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(180), 180)
    
    def test_syo_maukkaasti_ei_riita_maukkaat_maara(self):
        kassapaate = Kassapaate()
        kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(kassapaate.maukkaat, 0)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    #Edulliset kortti

    def test_syo_edullisesti_kortilla_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 1000 - 240)

    def test_syo_edullisesti_kortilla_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kortilla_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_ei_riita_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhamaksukortti)

        self.assertEqual(self.koyhamaksukortti.saldo, 100)
    
    def test_syo_edullisesti_kortilla_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.koyhamaksukortti), False)

    def test_syo_edullisesti_kortilla_edulliset_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhamaksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    #Maukkaat kortti

    def test_syo_maukkaasti_kortilla_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 1000 - 400)

    def test_syo_maukkaasti_kortilla_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_ei_riita_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhamaksukortti)

        self.assertEqual(self.koyhamaksukortti.saldo, 100)
    
    def test_syo_maukkaasti_kortilla_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.koyhamaksukortti), False)

    def test_syo_maukkaasti_kortilla_maukkaat_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhamaksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassassa_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_lataa_rahaa_negatiivinen_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(self.maksukortti.saldo, 1000)