import time

def geraTabuleiro():
    print('Lendo arquivo...')

    # Abre o arquivo com o tabuleiro
    f = open("tabuleiro.txt")

    # Ignora a primeira linha
    f.readline()

    # Inicializa o array do tabuleiro
    tabuleiro = []

    # Percorre o arquivo para preencher o array
    for i in range(9):
        try:
            linha = f.readline().split()
            # Verifica se a linha tem 9 números
            if len(linha) == 9:
                tabuleiro.append(linha)
            else:
                print("Tabuleiro informado inválido.")
                f.close()
                return False
        except Exception as e:
            print(repr(e))
            f.close()
            return False
    f.close()
    return tabuleiro

def printTabuleiro(tabuleiro):
    for i in range(9):
        linha = ''
        for j in range(9):
            linha += str(tabuleiro[i][j]) + ' '
            if j % 3 == 2 and j < 8:
                linha += '| '
        print(linha)
        if i % 3 == 2 and i < 8:
            print('-' * 21)

def encontraVazio(tabuleiro):
    # Percorre o tabuleiro
    for i in range(9):
        for j in range(9):
            # Verifica se é vazio
            if tabuleiro[i][j] == 'x':
                # Retorna a posição
                return (i, j)
    # Se não encontrou
    return None

def numeroValido(tabuleiro, linha, coluna, numero):
    # Verifica se o número já existe na linha
    if numero in tabuleiro[linha]:
        return False

    # Verifica se o número já existe na coluna
    for i in range(9):
        if tabuleiro[i][coluna] == numero:
            return False

    # Verifica se o número já exista na grade 3x3
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[inicio_linha + i][inicio_coluna + j] == numero:
                return False

    # Número válido
    return True

def buscaProfundidade(tabuleiro):
    # Encontra o próximo espaço vazio
    espacoVazio = encontraVazio(tabuleiro)

    # Verifica se encontrou algum espaço vazio
    if not espacoVazio:
        # Resolvido (não tem espaços vazios)
        return True

    # Recupera a posição do espaço vazio
    linha, coluna = espacoVazio

    # Percorre os números possíveis (de 1 a 9) até encotrar um válido para a posição
    for numero in range(1, 10):
        if numeroValido(tabuleiro, linha, coluna, str(numero)):
            tabuleiro[linha][coluna] = str(numero)

            # Chama a busca em profundidade para o próximo espaço
            if buscaProfundidade(tabuleiro):
                return True

            # Retorno o valor para vazio caso dê errado
            tabuleiro[linha][coluna] = 'x'

    return False

# Execução
tabuleiro = []

tabuleiro = geraTabuleiro()

printTabuleiro(tabuleiro)

# Inicia o timer
start = time.time()

if buscaProfundidade(tabuleiro):
    print(f"\nSolução Encontrada! Sudoku resolvido com sucesso em {time.time() - start:.2f}s:")
    printTabuleiro(tabuleiro)
else:
    print(f"\nSolução não Encontrada! Não foi possível resolver o Sudoku. Tempo decorrido: {time.time() - start:.2f}s")
