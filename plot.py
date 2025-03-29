'''
Visualização da variação do preço do m² ao longo do tempo
'''

import matplotlib.pyplot as plt
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
        plt.ylabel(f'{coluna_avaliar} por m²')
        plt.title("Gráfico de Barras")

        # rotariona os rótulos do eixo X para melhor visualização
        plt.xticks(np.arange(0, len(self._df), step=5), rotation=50, fontsize=10)

        # interatividade com o mouse no grafico
        mplcursors.cursor(hover=True)

        # exibi o gráfico
        plt.show()

def main():
    # LER O ARQUIVO ANTES
    leitor = Leitor_Excel("Preço-venda-aluguel.xlsx")
    df = leitor.ler_aquivo()  # DataFrame lido

    print("\nGRÁFICO DE PREÇOS DE VENDAS E ALUGUEIS POR METRO QUADRADO (R$/m²)")
    print("POSSÍVEIS COLUNAS A SEREM AVALIADAS:")
    opcoes_colunas = {
        1: 'venda',
        2: 'venda_1D',
        3: 'venda_2D',
        4: 'venda_3D',
        5: 'venda_4D',
        6: 'aluguel',
        7: 'aluguel_1D',
        8: 'aluguel_2D',
        9: 'aluguel_3D',
        10: 'aluguel_4D'
    }

    for k, v in opcoes_colunas.items():
        print(f"{k}. {v}")

    while True:
        try:
            escolha = int(input("\nQual coluna gostaria de visualizar? (1-10): "))
            if escolha in opcoes_colunas:
                coluna_avaliar = opcoes_colunas[escolha]
                break
            else:
                print("Digite um número entre 1 e 10.")
        except ValueError:
            print("Por favor, insira um número válido.")

    print(f"Você escolheu a coluna: {coluna_avaliar}")

    # Criando a análise de dados com o DataFrame lido
    analise = AnaliseDados(df)
    analise.criando_grafico(coluna_avaliar)

main()

