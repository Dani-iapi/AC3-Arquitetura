from operacoes import Operacoes
import math

class Calcular(Operacoes):
    def calculaSoma(self, valor1, valor2):
        return valor1 + valor2
    def calculaSubtracao(self, valor1, valor2):
        return valor1 - valor2
    def calculaDivisao(self, valor1, valor2):
        return valor1 / valor2
    def calculaMultiplicacao(self, valor1, valor2):
        return valor1 * valor2 
    def calculaRaiz(self, valor1, valor2):
        return valor1 ** (1/valor2)
    def calculaPotencia(self, valor1, valor2):
        return math.pow(valor1, valor2)

