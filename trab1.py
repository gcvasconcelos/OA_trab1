def criaIndices(arquivo, nome_arquivo_indices):
    arq_indices = open(nome_arquivo_indices, 'w+')
    for linha in arquivo:
        dados = linha.split()
        nome = ' '.join(dados[1:-3])
        matricula = dados[0]
        indice = matricula + '$' + nome
        arq_indices.write(indice + '\n')
    arq_indices.close()
    return

def printaArquivo(arquivo):
    print('MATRIC\tNOME\t\t\t\tOP\tCURSO\tTURMA')
    for linha in arquivo:
        dados = linha.split()
        print(dados[0] + '\t' + ' '.join(dados[1:-3]) + '\t\t' + dados[-3] + '\t' + dados[-2] + '\t' + dados[-1])
    return


lista1 = open('benchmarks/lista1.txt', 'r')
# printaArquivo(lista1)
criaIndices(lista1, 'indicelista1.ind')
lista1.close()