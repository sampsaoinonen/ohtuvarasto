import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)
    
    def test_lisays_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(100)
        self.assertEqual(self.varasto.saldo, 10)

    def test_ottaminen_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(10)
        self.assertEqual(otettu, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_ottaminen_saldon_verran(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(5)
        self.assertEqual(otettu, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_konstruktori_negatiivisella_tilavuudella(self):
        varasto_negatiivisella = Varasto(-10)
        self.assertEqual(varasto_negatiivisella.tilavuus, 0)

    def test_konstruktori_negatiivisella_saldolla(self):
        varasto_negatiivisella = Varasto(10, -10)
        self.assertEqual(varasto_negatiivisella.saldo, 0)
    
    def test_ota_varastosta_ei_ota_negatiivista_maaraa(self):
        varasto = Varasto(10, 5)
        otettu = varasto.ota_varastosta(-3)
        self.assertEqual(otettu, 0)
        self.assertEqual(varasto.saldo, 5)

    def test_varasto_str(self):    
        varasto = Varasto(10, 2)
        expected_str = "saldo = 2, vielä tilaa 8"    
        self.assertEqual(str(varasto), expected_str)


    
