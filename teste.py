import unittest
from calcula import Calcular

class TesteCalculadora(unittest.TestCase):
    def test_soma(self):
        soma = Calcular().calculaSoma(10,2)
        self.assertEqual (soma, 12)

    def test_subtracao(self):
        subtracao = Calcular().calculaSubtracao(350, 100)
        self.assertEqual (subtracao, 250)

    def test_multiplicacao(self):
        multiplicacao = Calcular().calculaMultiplicacao(2,3)
        self.assertEqual (multiplicacao, 6)

    def test_divisao(self):
        divisao = Calcular().calculaDivisao(30, 2)
        self.assertEqual (divisao, 15)
   
    def test_potencia(self):
        potencia = Calcular().calculaPotencia(8, 2)
        self.assertEqual (potencia, 16)

    def test_raiz(self):
        raiz = Calcular().calculaRaiz(16, 2)
        self.assertEqual (raiz, 4)

if __name__ == '__main__':
    unittest.main()

