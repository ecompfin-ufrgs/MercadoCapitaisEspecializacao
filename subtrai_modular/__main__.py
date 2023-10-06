"""
Programa subtrai.py
Descrição: Este programa lê dois números do teclado, calcula o resultado da subtração e coloca o resultado na tela.
Autor: Nelson Seixas dos Santos
Data: 05/10/2023
Versão: 0.0.2
"""




# Definição de funções

def main():
    # Importação de módulos
    import es
    import operacao

    # Atribuição de variáveis
    subtracao: float = 0.0
    dados: list = []

    # Entrada de dados
    dados = es.entrada()

    # Processamento de dados
    subtracao = operacao.subtrai(dados[0], dados[1])

    # Saída de dados
    es.saida(dados[0], dados[1], subtracao)


    

# Chamada da função principal

if __name__ == "__main__":
    main()







