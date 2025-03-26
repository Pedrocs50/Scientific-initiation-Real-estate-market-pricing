import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("CÁLCULO DO YIELD (RELAÇÃO ENTRE ALUGUEL E VENDA)")
    print("POSSÍVEIS COLUNAS DE VENDA")
    print("1. Venda geral")
    print("2. Venda com 1 dormitório")
    print("3. Venda com 2 dormitórios")
    print("4. Venda com 3 dormitórios")
    print("5. Venda com 4 dormitórios\n")

    print("POSSÍVEIS COLUNAS DE ALUGUEL")
    print("6. Aluguel geral")
    print("7. Aluguel com 1 dormitório")
    print("8. Aluguel com 2 dormitórios")
    print("9. Aluguel com 3 dormitório")
    print("10. Aluguel com 4 dormitório\n")

    while True:
        venda_coluna = int(input("Escolha a coluna de venda (1-5): "))
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

    while True:
        aluguel_coluna = int(input("Escolha a coluna de aluguel (6-10): "))
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

    arquivo = "Preço-venda-aluguel.xlsx"  
    df = pd.read_excel(arquivo, thousands=',', decimal='.')

    # garantindo que as colunas selecionadas são numéricas
    df[aluguel_coluna] = pd.to_numeric(df[aluguel_coluna], errors='coerce')
    df[venda_coluna] = pd.to_numeric(df[venda_coluna], errors='coerce')

    # calculando o Yield
    df['yield'] = df[aluguel_coluna] / df[venda_coluna]

    # Exibir os dados
    print(f"Coluna de venda escolhida: {venda_coluna}")
    print(f"Coluna de aluguel escolhida: {aluguel_coluna}")
    print(f"Primeiras linhas dos dados calculados de yield:\n{df[['Data', venda_coluna, aluguel_coluna, 'yield']].head()}")

    # plotando o gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(df["Data"], df['yield'], color="green")
    plt.xlabel("Data")
    plt.ylabel("Yield (Aluguel / Venda)")
    plt.title(f"Gráfico de Yield entre {aluguel_coluna} e {venda_coluna}")
    plt.xticks(rotation=45)

    # exibi o gráfico
    plt.show()

main()
