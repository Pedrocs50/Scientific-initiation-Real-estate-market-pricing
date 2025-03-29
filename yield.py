import pandas as pd
import matplotlib.pyplot as plt
from ler_arquivo import Leitor_Excel
import numpy as np
import mplcursors

class Yield:
    def __init__(self, df, aluguel_coluna, venda_coluna):
        self._df = df
        self.aluguel_coluna = aluguel_coluna
        self.venda_coluna = venda_coluna

    def calcular_yield(self):
        if self._df is None or self._df.empty:
            print("Erro: Necessário que um arquivo seja lido para criar o gráfico.")
            return

        # garante que as colunas sejam numéricas
        self._df[self.aluguel_coluna] = pd.to_numeric(self._df[self.aluguel_coluna], errors='coerce')
        self._df[self.venda_coluna] = pd.to_numeric(self._df[self.venda_coluna], errors='coerce')

        # calculando o aluguel anual
        self._df['aluguel_anual'] = self._df[self.aluguel_coluna] * 12

        # calculando o Yield
        self._df['yield'] = (self._df['aluguel_anual'] / self._df[self.venda_coluna]) * 100

        # exibe os dados
        print(f"Coluna de venda escolhida: {self.venda_coluna}")
        print(f"Coluna de aluguel escolhida: {self.aluguel_coluna}")
        pd.set_option('display.max_rows', None)
        print(f"Todas as linhas dos dados calculados de yield:\n{self._df[['Data', self.venda_coluna, self.aluguel_coluna, 'yield']].round(2)}")


        # Plotando o gráfico
        plt.figure(figsize=(12, 6))
        plt.plot(self._df["Data"], self._df['yield'], color="green")
        plt.xlabel("Data")
        plt.ylabel("Yield (Aluguel / Venda)")
        plt.title(f"Gráfico de Yield entre {self.aluguel_coluna} e {self.venda_coluna}")
        plt.xticks(np.arange(0, len(self._df), step=5), rotation=50, fontsize=10)

        mplcursors.cursor(hover=True)


        # exibe o gráfico
        plt.show()

def main():
    # LER O ARQUIVO ANTES
    leitor = Leitor_Excel("Preço-venda-aluguel.xlsx")
    df = leitor.ler_aquivo()  # DataFrame lido

    if df is None or df.empty:
        print("Erro: O arquivo não pôde ser carregado. Verifique o caminho e tente novamente.")
        return

    print("\nGRÁFICO DE PREÇOS DE VENDAS E ALUGUEIS POR METRO QUADRADO (R$/m²)")

    # escolha da coluna de venda
    while True:
        print("\nEscolha a coluna de venda (1-5):")
        print("1. venda")
        print("2. venda_1D")
        print("3. venda_2D")
        print("4. venda_3D")
        print("5. venda_4D")
        try:
            venda_coluna = int(input("\nEscolha a coluna de venda (1-5): "))
            if 1 <= venda_coluna <= 5:
                if venda_coluna == 1:
                    venda_coluna = 'venda'
                elif venda_coluna == 2:
                    venda_coluna = 'venda_1D'
                elif venda_coluna == 3:
                    venda_coluna = 'venda_2D'
                elif venda_coluna == 4:
                    venda_coluna = 'venda_3D'
                elif venda_coluna == 5:
                    venda_coluna = 'venda_4D'
                break
            else:
                print("Escolha uma coluna de venda válida.")
        except ValueError:
            print("Por favor, insira um número válido.")

    # escolha da coluna de aluguel
    while True:
        print("\nEscolha a coluna de aluguel (6-10):")
        print("6. aluguel")
        print("7. aluguel_1D")
        print("8. aluguel_2D")
        print("9. aluguel_3D")
        print("10. aluguel_4D")
        try:
            aluguel_coluna = int(input("\nEscolha a coluna de aluguel (6-10): "))
            if 6 <= aluguel_coluna <= 10:
                if aluguel_coluna == 6:
                    aluguel_coluna = 'aluguel'
                elif aluguel_coluna == 7:
                    aluguel_coluna = 'aluguel_1D'
                elif aluguel_coluna == 8:
                    aluguel_coluna = 'aluguel_2D'
                elif aluguel_coluna == 9:
                    aluguel_coluna = 'aluguel_3D'
                elif aluguel_coluna == 10:
                    aluguel_coluna = 'aluguel_4D'
                break
            else:
                print("Escolha uma coluna de aluguel válida.")
        except ValueError:
            print("Por favor, insira um número válido.")

    # calcular e mostrar o gráfico de Yield
    analise = Yield(df, aluguel_coluna, venda_coluna)
    analise.calcular_yield()

main()


'''
Cálculo:
Yield(%) = (Aluguel anual/Preço da Venda) x 100

No contexto de aluguel e venda, o yield é uma métrica que relaciona o retorno de um investimento (no caso, o aluguel) com o valor de mercado do bem (no caso, o preço de venda). Ele é uma medida importante para investidores que querem saber qual o retorno que estão obtendo com o aluguel em relação ao valor de venda do imóvel.

O yield vai indicar a rentabilidade do aluguel em relação ao preço de venda. Quanto maior o valor de yield, mais vantajoso é o aluguel em relação ao preço de venda do imóvel.

'''