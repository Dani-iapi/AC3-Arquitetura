from abc import ABC, abstractmethod

class Operacoes(ABC):
    @abstractmethod
    def calculaSoma(self, valor1, valor2):
        pass

    @abstractmethod
    def calculaSubtracao(self, valor1, valor2):
        pass

    @abstractmethod
    def calculaDivisao(self, valor1, valor2):
        pass

    @abstractmethod
    def calculaMultiplicacao(self, valor1, valor2):
        pass
    
    @abstractmethod
    def calculaPotencia(self, valor1, valor2):
        pass

    @abstractmethod
    def calculaRaiz(self, valor1, valor2):
        pass
