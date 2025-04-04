'''
TAXAS IGP-M DE 2008 ATÉ 2025
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from ler_arquivo import Leitor_Excel
import numpy as np
import mplcursors

class AnaliseDados:
    def __init__(self, df):
        self._df = df

    def criando_grafico(self, coluna_avaliar):
        if self._df is None:
            print("Erro: Necessário que um arquivo seja lido, para criar o gráfico.")
            return

        plt.figure(figsize=(12, 6))  # Define o tamanho do gráfico
        plt.plot(self._df["Data"], self._df[coluna_avaliar], color="blue")  # o primeiro é o eixo 'X' e o segundo é o eixo 'Y'

        # configurando os rótulos e título
        plt.xlabel("Data")
        plt.ylabel(f'{coluna_avaliar}')
        plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100))
        plt.title("Gráfico de Linhas")
        
        # interatividade com o mouse no grafico
        mplcursors.cursor(hover=True)

        # exibi o gráfico
        plt.show()

def main():
    # LER O ARQUIVO ANTES
    leitor = Leitor_Excel("Dados-IGP-M.xlsx")
    df = leitor.ler_aquivo_vendas_aluguel()  # DataFrame lido

    print("\nGRÁFICO DA TAXA IPCA 2008 ATÉ 2025")
    opcoes_colunas = {
        1: 'IGP-M'
    }

    for k, v in opcoes_colunas.items():
        print(f"{k}. {v}")

    while True:
        try:
            escolha = int(input("\nQual coluna gostaria de visualizar? (1-2): "))
            if escolha in opcoes_colunas:
                coluna_avaliar = opcoes_colunas[escolha]
                break
            else:
                print("Digite um número entre 1 a 2.")
        except ValueError:
            print("Por favor, insira um número válido.")

    print(f"Você escolheu a coluna: {coluna_avaliar}")

    # Criando a análise de dados com o DataFrame lido
    analise = AnaliseDados(df)
    analise.criando_grafico(coluna_avaliar)

main()

