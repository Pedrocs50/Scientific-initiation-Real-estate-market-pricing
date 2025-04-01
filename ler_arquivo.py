import pandas as pd

class Leitor_Excel:
    def __init__(self, arquivo):
        self._arquivo = arquivo
        self._df = None

    def ler_aquivo_vendas_aluguel(self):
        self._df = pd.read_excel(self._arquivo, decimal=',', thousands='.')
        print(self._df.head())  # Para conferir se os dados foram carregados
        return self._df
    
    def ler_aquivo_IPCA(self):
        self._df = pd.read_excel(self._arquivo)
        print(self._df.head())  # Para conferir se os dados foram carregados
        return self._df
