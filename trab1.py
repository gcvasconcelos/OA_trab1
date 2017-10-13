def printa_arquivo(arquivo):
    # print('MATRIC\tNOME\t\t\t\tOP\tCURSO\tTURMA')
    dados_arquivo = []
    for linha in arquivo:
        dados = linha.split()
        tamanho_nome = len(' '.join(dados[1:-3]))
        tabs = '\t\t'
        if tamanho_nome >= 24:
            tabs = '\t'
        # print(dados[0] + '\t' + ' '.join(dados[1:-3]) + tabs + dados[-3] + '\t' + dados[-2] + '\t' + dados[-1])
        dados_arquivo.append(dados)
    return dados_arquivo

def cria_indices(dados, indices):
    referencia = 0
    linhas = []
    chaves_primarias = []
    for i in range(len(dados)):
        matricula = str(dados[i][0])
        nome = ''.join(dados[i][1:-3])
        chave_primaria = matricula + '$' + nome
        chaves_primarias.append(chave_primaria)
        linhas.append(chave_primaria[0:30] + '\t' + str(referencia) + '\n')
        referencia += 1
    indices.writelines(linhas)
    return chaves_primarias

def cria_indices_secundarios(arq_op, arq_turma, primaria, dados):
    ops = []
    turmas = []
    HEAD_op = [-1]
    HEAD_turma = [-1, -1]
    for i in range(len(dados)):
        if dados[i][-3] not in ops:
            ops.append(dados[i][-3])
        if dados[i][-1] not in turmas:
            turmas.append(dados[i][-1])
    for i in range(len(dados)):
        if dados[i][-3] in ops:
            arq_op.write(primaria[i] + '\t' + str(HEAD_op[0]) + '\n')
            HEAD_op[0] = i
        if dados[i][-1] in turmas:
            arq_turma.write(primaria[i] + '\t' + str(HEAD_turma[turmas.index(dados[i][-1])]) + '\n')
            HEAD_turma[turmas.index(dados[i][-1])] = i
    return


lista1 = open('benchmarks/lista1.txt', 'r')
dados_arquivo = printa_arquivo(lista1)
indices1 = open('indice_lista1.ind', 'w')
pks = cria_indices(dados_arquivo, indices1)
secundario_op = open('op_lista1.ind', 'w+')
secundario_turma = open('turma_lista1.ind', 'w+')
cria_indices_secundarios(secundario_op, secundario_turma, pks, dados_arquivo)

lista1.close()
indices1.close()
secundario_op.close()
secundario_turma.close()