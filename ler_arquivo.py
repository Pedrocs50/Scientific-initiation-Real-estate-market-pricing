import pandas as pd

class Leitor_Excel:
    def __init__(self, arquivo):
        self._arquivo = arquivo
        self._df = None

    def ler_aquivo(self):
        self._df = pd.read_excel(self._arquivo, thousands=',', decimal='.')
        print(self._df.head())  # Para conferir se os dados foram carregados
        return self._df
