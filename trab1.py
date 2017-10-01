def cria_indices(arquivo, nome_arquivo_primario):
    arq_primario = open(nome_arquivo_primario, 'w+')
    referencia = 0
    for linha in arquivo:
        dados = linha.split()
        nome = ' '.join(dados[1:-3])
        matricula = dados[0]
        chave_primaria = matricula + '$' + nome
        arq_primario.write(chave_primaria[0:30] + '\t' + str(referencia) + '\n')
        referencia += 1
    arq_primario.close()
    return


def cria_indices_secundarios(arquivo, nome_arquivo_secundario):
    arq_secundario1 = open(nome_arquivo_secundario + '1', 'w+')
    arq_secundario2 = open(nome_arquivo_secundario + '2', 'w+')
    for linha in arquivo:
        dados = linha.split()
        op = dados[-3]
        turma = dados[-1]
    arq_secundario1.close()
    arq_secundario2.close()
    return


def printa_arquivo(arquivo):
    print('MATRIC\tNOME\t\t\t\tOP\tCURSO\tTURMA')
    for linha in arquivo:
        dados = linha.split()
        print(dados[0] + '\t' + ' '.join(dados[1:-3]) + '\t\t' + dados[-3] + '\t' + dados[-2] + '\t' + dados[-1])
    return


lista1 = open('benchmarks/lista1.txt', 'r')
# printa_arquivo(lista1)
cria_indices(lista1, 'indicelista1.ind')
lista1.close()
