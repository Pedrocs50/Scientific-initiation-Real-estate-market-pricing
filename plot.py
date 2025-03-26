import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("GRÁFICO DE PREÇOS DE VENDAS E ALUGUEIS POR METRO QUADRADO(R$/m²)")
    print("POSSÍVES COLUNAS A SEREM AVALIADAS")
    print("1. Venda geral")
    print("2. Venda com 1 dormitório")
    print("3. Venda com 2 dormitórios")
    print("4. Venda com 3 dormitórios")
    print("5. Venda com 4 dormitórios")
    print("6. Aluguel geral")
    print("7. Aluguel com 1 dormitório")
    print("8. Aluguel com 2 dormitório")
    print("9. Aluguel com 3 dormitório")
    print("10. Aluguel com 4 dormitório\n")

    while True:
        coluna_avaliar = int(input("Qual coluna gostaria de visualizar? (1-10): "))

        if 1 <= coluna_avaliar <= 10:
            if coluna_avaliar == 1:
                coluna_avaliar = 'venda'
            elif coluna_avaliar == 2:
                coluna_avaliar = 'venda_1D'
            elif coluna_avaliar == 3:
                coluna_avaliar = 'venda_2D'
            elif coluna_avaliar == 4:
                coluna_avaliar = 'venda_3D'
            elif coluna_avaliar == 5:
                coluna_avaliar = 'venda_4D'
            elif coluna_avaliar == 6:
                coluna_avaliar = 'aluguel'
            elif coluna_avaliar == 7:
                coluna_avaliar = 'aluguel_1D'
            elif coluna_avaliar == 8:
                coluna_avaliar = 'aluguel_2D'
            elif coluna_avaliar == 9:
                coluna_avaliar = 'aluguel_3D'
            elif coluna_avaliar == 10:
                coluna_avaliar = 'aluguel_4D'
            
            print(f"Você escolheu a coluna: {coluna_avaliar}")
            break  
        else:
            print("Digite um valor válido entre 1 e 10.")  

    
    arquivo = "Preço-venda-aluguel.xlsx"

    # carregando os dados para depois exibilos e, substituindo as vírgulas por pontos, para evitar erros
    df = pd.read_excel(arquivo, thousands=',', decimal='.')
    print(df.head())  

    # criando o gráfico de barras
    plt.figure(figsize=(12, 6))  # Define o tamanho do gráfico
    plt.bar(df["Data"], df[coluna_avaliar], color="blue")  # o primeiro é o eixo 'X' e o segundo é o eixo 'Y'

    # configurando os rótulos e título
    plt.xlabel("Data")
    plt.ylabel(f'{coluna_avaliar} por m²')
    plt.title("Gráfico de Barras")

    # rotariona os rótulos do eixo X para melhor visualização
    plt.xticks(rotation=45)

    # exibi o gráfico
    plt.show()

main()
