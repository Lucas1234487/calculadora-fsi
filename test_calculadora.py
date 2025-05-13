import unittest
from calculadora import calcular

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calcular("2", "+", "3"), 5.0)

    def test_subtracao(self):
        self.assertEqual(calcular("5", "-", "2"), 3.0)

    def test_multiplicacao(self):
        self.assertEqual(calcular("3", "*", "4"), 12.0)

    def test_divisao(self):
        self.assertEqual(calcular("10", "/", "2"), 5.0)

    def test_exponenciacao(self):
        self.assertEqual(calcular("2", "^", "3"), 8.0)

    def test_divisao_por_zero(self):
        self.assertIsNone(calcular("5", "/", "0"))

    def test_operador_invalido(self):
        self.assertIsNone(calcular("4", "?", "2"))

    def test_valor_invalido(self):
        self.assertIsNone(calcular("a", "+", "2"))

    def test_valor_invalido2(self):
        self.assertIsNone(calcular("2", "+", "b"))

    def test_ambos_invalidos(self):
        self.assertIsNone(calcular("x", "/", "y"))

    def test_negativos(self):
        self.assertEqual(calcular("-2", "*", "-3"), 6.0)

    def test_zero(self):
        self.assertEqual(calcular("0", "+", "0"), 0.0)

    def test_float(self):
        self.assertAlmostEqual(calcular("3.5", "*", "2"), 7.0)

    def test_expoente_zero(self):
        self.assertEqual(calcular("5", "^", "0"), 1.0)

    def test_zero_expoente(self):
        self.assertEqual(calcular("0", "^", "5"), 0.0)

    def test_sub_neg_result(self):
        self.assertEqual(calcular("2", "-", "5"), -3.0)

    def test_expoente_negativo(self):
        self.assertAlmostEqual(calcular("2", "^", "-2"), 0.25)

    def test_div_float(self):
        self.assertAlmostEqual(calcular("7", "/", "2"), 3.5)

    def test_multiplicando_zero(self):
        self.assertEqual(calcular("0", "*", "999"), 0.0)

    def test_grande(self):
        self.assertEqual(calcular("100000", "+", "250000"), 350000.0)

if __name__ == '__main__':
    unittest.main()