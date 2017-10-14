def inicializa_registros(arquivo):
    registros = []
    for linha in arquivo:
        registro = {}
        dados = linha.split()
        registro['matric'] = dados[0]
        registro['nome'] = ' '.join(dados[1:-3])
        registro['op'] = dados[-3]
        registro['curso'] = dados[-2]
        registro['turma'] = dados[-1]
        registros.append(registro)
    return registros

def inicializa_indices(arq_indices, registros):
    indices = []
    posicao = 0
    for registro in registros:
        indice = {}
        chave_primaria = registro['matric'] + '#' + registro['nome']
        chave_primaria = chave_primaria[0:30]
        indice['pk'] = chave_primaria
        indice['posicao'] = posicao
        indices.append(indice)
        posicao += 1
        arq_indices.write(indice['pk'] + '\t' + str(indice['posicao']) + '\n')
    return indices

def opcoes_secundario(registros, ind_secundario):
    opcoes = []
    for registro in registros:
        if registro[ind_secundario] not in opcoes:
            opcoes.append(registro[ind_secundario])
    return opcoes

def inicializa_indice_secundario(arq_secundario, registros, indices, ind_secundario):
    opcoes = opcoes_secundario(registros, ind_secundario)
    head = []
    for i in range(len(opcoes)):
        head.append(-1)
    i = 0
    for registro in registros:
        if registro[ind_secundario] in opcoes:
            foo = opcoes.index(registro[ind_secundario])
            arq_secundario.write(indices[i]['pk'] + '\t' + registro[ind_secundario] + '\t' + str(head[foo]) + '\n')
            head[foo] = indices[i]['posicao']
        i += 1
    return

lista1 = open('benchmarks/lista1.txt', 'r')
registros = inicializa_registros(lista1)
lista1.close()

indices1 = open('indice_lista1.ind', 'w+')
indices = inicializa_indices(indices1, registros)
indices1.close()

secundario_op = open('op_lista1.ind', 'w+')
secundario_turma = open('turma_lista1.ind', 'w+')
inicializa_indice_secundario(secundario_op, registros, indices, 'op')
inicializa_indice_secundario(secundario_turma, registros, indices, 'turma')
secundario_op.close()
secundario_turma.close()