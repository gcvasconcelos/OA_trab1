# Parametros: um array, e duas posicoes no array
# Troca dois elementos de posicao no array
def troca_valores(array, i, j):
    array[i], array[j] = array[j], array[i]

# Parametros: um array, sua posicao final e inicial
# Transforma um array em um heap
def heapify(array, comeco, fim):
    esquerda = 2 * comeco + 1
    direita = 2 * (comeco + 1)
    maximo = comeco
    if (esquerda < fim) and (array[comeco] < array[esquerda]):
        maximo = esquerda
    if direita < fim and array[maximo] < array[direita]:
        maximo = direita
    if maximo != comeco:
        troca_valores(array, comeco, maximo)
        heapify(array, maximo, fim)
    return

# Ordena um array por meio de um heapsort
def heapsort(array):
    fim = len(array)
    comeco = fim // 2 - 1
    for i in range(comeco, -1, -1):
        heapify(array, i, fim)
    for i in range(fim - 1, 0, -1):
        troca_valores(array, i, 0)
        heapify(array, 0, i)
    return

# Variavel global que conta a quantidade de registros
num_registros = 0

# A partir de um arquivio de registros, separa os campos e os coloca nas devidas variaveis
# de uma lista de registros 
def inicializa_registros(arquivo):
    global num_registros
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
        num_registros += 1
    return registros

# Gera chaves primarias de uma lista de registros e cria uma lista com elas e suas posicoes
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
        arq_indices.write(indice['pk'] + ' ' * (2 + (30 - len(indice['pk']))) + str(indice['posicao']) + '\n')
    return indices

# Ordena os indices por chave primaria (matricula + nome)
def ordena_indices(arq_indices, indices):
    arq_indices.seek(0, 0)
    heapsort(indices)
    for indice in indices:
        arq_indices.write(indice['pk'] + ' ' * (2 + (30 - len(indice['pk']))) + str(indice['posicao']) + '\n')
    return


def opcoes_secundario(registros, ind_secundario):
    opcoes = []
    for registro in registros:
        if registro[ind_secundario] not in opcoes:
            opcoes.append(registro[ind_secundario])
    return opcoes

# Encontra um registro por meio da chave primaria
def busca_registro(chave_primaria, ind_secundario, registros):
    for registro in registros:
        pk = registro['matric'] + '#' + registro['nome']
        pk = pk[0:30]
        if chave_primaria == pk:
            return registro[ind_secundario]
    return None

# Cria o arquivo de indices secundarios usando os registros e os indices secundarios
def inicializa_indice_secundario(arq_secundario, registros, indices, ind_secundario):
    opcoes = opcoes_secundario(registros, ind_secundario)
    head = []
    for i in range(len(opcoes)):
        head.append(-1)

    for indice in indices:
        sk = busca_registro(indice['pk'], ind_secundario, registros)
        for opcao in opcoes:
            if sk == opcao:
                foo = opcoes.index(opcao)
                arq_secundario.write(
                    str(indice['posicao']) + '\t' + indice['pk'] + ' ' * (2 + (30 - len(indice['pk']))) + str(
                        head[foo]) + '\n')
                head[foo] = indice['posicao']
    return


def printa_arquivo(arquivo):
    for linha in arquivo:
        print(linha)
    return

# Adiciona um novo registro a todos os arquivos, mudando as listas invertidas dos indices secundarios
def adicionar_registro(arq_registros, arq_indices, arq_secundario_op, arq_secundario_turma, registros, indices,
                       novo_registro):
    global num_registros
    registros.append(novo_registro)
    arq_registros.write(# escreve o novo registro no arquivo contendo todos
        '\n' + novo_registro['matric'] + ' ' + novo_registro['nome'] + ' ' * (41 - len(novo_registro['nome'])) +
        novo_registro['op'] + ' ' * 4 +
        novo_registro['curso'] + ' ' * 9 + novo_registro['turma'])

    indice = {}
    chave_primaria = novo_registro['matric'] + '#' + novo_registro['nome']
    chave_primaria = chave_primaria[0:30]
    indice['pk'] = chave_primaria
    indice['posicao'] = num_registros
    num_registros += 1
    indices.append(indice)
    ordena_indices(arq_indices, indices)

    # Atualiza os indices secundarios
    inicializa_indice_secundario(arq_secundario_op, registros, indices, 'op')
    inicializa_indice_secundario(arq_secundario_turma, registros, indices, 'turma')
    return

# Remove um registro de todos os arquivos a partir por meio da matricula
def remover_registros(arq_registros, arq_indices, arq_secundario_op, arq_secundario_turma, registros, indices, matric_remover):
    posicao_remover = -1
    for i in range(0, len(registros)):
        if registros[i]['matric'] == matric_remover:
            posicao_remover = i
    if posicao_remover == -1:# verifica se o registro estarios
        for indice in indices:
            arq_indices.write(indice['pk']+str(indice['posicao'])+'\n')
            if i != final:
                arq_indices.write('\n')
            i += 1
            # Atualiza os indices secundarios
    inicializa_indice_secundario(arq_secundario_op, registros, indices, 'op')
    inicializa_indice_secundario(arq_secundario_turma, registros, indices, 'turma')
    return

# Inicializacao dos registros
arq_registros1 = open('benchmarks/lista1.txt', 'r')
registros1 = inicializa_registros(arq_registros1)
arq_registros1.close()
arq_registros2 = open('benchmarks/lista2.txt', 'r')
registros2 = inicializa_registros(arq_registros2)
arq_registros2.close()

# Criacao dos indices primarios
arq_indices1 = open('indice_lista1.ind', 'w+')
indices1 = inicializa_indices(arq_indices1, registros1)
ordena_indices(arq_indices1, indices1)
arq_indices1.close()
arq_indices2 = open('indice_lista2.ind', 'w+')
indices2 = inicializa_indices(arq_indices2, registros2)
ordena_indices(arq_indices2, indices2)
arq_indices2.close()

# Criacao dos indices secundarios
secundario_op1 = open('op_lista1.ind', 'w+')
secundario_turma1 = open('turma_lista1.ind', 'w+')
inicializa_indice_secundario(secundario_op1, registros1, indices1, 'op')
inicializa_indice_secundario(secundario_turma1, registros1, indices1, 'turma')
secundario_op1.close()
secundario_turma1.close()
secundario_op2 = open('op_lista2.ind', 'w+')
secundario_turma2 = open('turma_lista2.ind', 'w+')
inicializa_indice_secundario(secundario_op2, registros2, indices2, 'op')
inicializa_indice_secundario(secundario_turma2, registros2, indices2, 'turma')
secundario_op2.close()
secundario_turma2.close()


print('Qual arquivo voce deseja abrir?')
print('1.\tlista1.txt')
print('2.\tlista2.txt')
opcao_arquivo = input('Digite o numero correspondente a sua opcao: ')
if opcao_arquivo == 1:
    nome_registros = 'benchmarks/lista1.txt'
    nome_indices = 'indice_lista1.ind'
    nome_indices_op = 'op_lista1.ind'
    nome_indices_turma = 'turma_lista1.ind'
    registros = registros1
    indices = indices1
elif opcao_arquivo == 2:
    nome_registros = 'benchmarks/lista2.txt'
    nome_indices = 'indice_lista2.ind'
    nome_indices_op = 'op_lista2.ind'
    nome_indices_turma = 'turma_lista2.ind'
    registros = registros2
    indices = indices2


print('\n\tMenu')
print('1.\tVisualizar arquivos')
print('2.\tIncluir registro')
print('3.\tExcluir registro')
print('4.\tAtualizar registro')
opcao_menu = input('Digite o numero correspondente a sua opcao: ')
if opcao_menu == 1:
    print('\n1.\tArquivo de dados')
    print('2.\tArquivo de indices primarios')
    print("3.\tArquivo de indice secundario 'OP'")
    print("4.\tArquivo de indice secundario 'TURMA'\n")
    opcao_print = input('Digite o numero correspondente a sua opcao: ')
    if opcao_print == 1:
        arquivo = open(nome_registros, 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    elif opcao_print == 2:
        arquivo = open(nome_indices, 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    elif opcao_print == 3:
        arquivo = open(nome_indices_op, 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    elif opcao_print == 4:
        arquivo = open(nome_indices_turma, 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    else:
        print('Opcao invalida')
elif opcao_menu == 2:
    print('\n')
    novo_registro = {}
    novo_registro['matric'] = raw_input('Digite a matricula: ')
    novo_registro['nome'] = raw_input('Digite o nome: ')
    novo_registro['op'] = raw_input('Digite o OP: ')
    novo_registro['curso'] = raw_input('Digite a curso: ')
    novo_registro['turma'] = raw_input('Digite a turma: ')

    arq_registros = open(nome_registros, 'r')
    print('\nArquivo de indices primarios antes da inclusao:')
    printa_arquivo(arq_registros)

    arq_registros = open(nome_registros, 'a')
    arq_indices = open(nome_indices, 'w+')
    arq_secundario_op = open(nome_indices_op, 'w')
    arq_secundario_turma = open(nome_indices_turma, 'w')
    adicionar_registro(arq_registros, arq_indices, arq_secundario_op, arq_secundario_turma, registros, indices,
                       novo_registro)

    arq_registros = open(nome_registros, 'r')
    print('\nArquivo de indices primarios apos a inclusao')
    printa_arquivo(arq_registros)

    arq_registros.close()
    arq_indices.close()
    arq_secundario_op.close()
    arq_secundario_turma.close()
elif opcao_menu == 3:
    print ('\n')
    matricula_remover = str(raw_input('Digite a matricula do registro a ser removido'))
    
    arquivo = open(nome_indices, 'r')
    print('\nArquivo de indices primarios antes da exclusao:')
    printa_arquivo(arquivo)
    arquivo.close()

    arq_registros = open(nome_registros, 'w')
    arq_indices = open(nome_indices, 'w+')
    arq_secundario_op = open(nome_indices_op, 'a')
    arq_secundario_turma = open(nome_indices_turma, 'a')
    remover_registros(arq_registros, arq_indices, arq_secundario_op, arq_secundario_turma, registros, indices, matricula_remover)
    

    arq_registros = open(nome_registros, 'r')
    print('\nArquivo de indices primarios apos a exclusao')
    printa_arquivo(arq_registros)
    
    arq_registros.close()
    arq_indices.close()
    arq_secundario_op.close()
    arq_secundario_turma.close()
elif opcao_menu == 4:
    print('\n')
    matric_atualizar = raw_input('Qual matricula deseja atualizar?')
    
    arquivo = open(nome_indices, 'r')
    print('\nArquivo de indices primarios antes da atualizacao:')
    printa_arquivo(arquivo)
    arquivo.close()

    posicao_atualizar = -1
    for i in range(0, len(registros)):
        if registros[i]['matric'] == matric_atualizar:
            posicao_atualizar = i
    if posicao_atualizar == -1:# verificacao: ')
        dado = str(raw_input('Digite o valor do novo campo: '))
        new_registro = {}
        new_registro['matric'] = registros[posicao_atualizar]['matric']
        new_registro['nome'] = registros[posicao_atualizar]['nome']
        new_registro['op'] = registros[posicao_atualizar]['op']
        new_registro['curso'] = registros[posicao_atualizar]['curso']
        new_registro['turma'] = registros[posicao_atualizar]['turma']
        if campo_atualizar == 1:# atualiza o dado escolhido com a informacao dada
            new_registro['matric'] = dado
        elif campo_atualizar == 2:
            new_registro['nome'] = dado
        elif campo_atualizar == 3:
            new_registro['op'] = dado
        elif campo_atualizar == 4:
            new_registro['curso'] = dado
        elif campo_atualizar == 5:
            new_registro['turma'] = dado

        arq_registros = open(nome_registros, 'w')
        arq_indices = open(nome_indices, 'w+')
        arq_secundario_op = open(nome_indices_op, 'w')
        arq_secundario_turma = open(nome_indices_turma, 'w')
        remover_registros(arq_registros, arq_indices, arq_secundario_op, arq_secundario_turma, registros, indices,
                          matric_atualizar)
        arq_registros = open(nome_registros, 'a')
        arq_indices = open(nome_indices, 'w+')
        arq_secundario_op = open(nome_indices_op, 'w')
        arq_secundario_turma = open(nome_indices_turma, 'w')
        adicionar_registro(arq_registros, arq_indices, arq_secundario_op, arq_secundario_turma, registros, indices,
                           new_registro)
        
        arq_registros = open(nome_registros, 'r')
        print('\nArquivo de indices primarios apos a atualizacao')
        printa_arquivo(arq_registros)
        
        arq_registros.close()
        arq_indices.close()
        arq_secundario_op.close()
        arq_secundario_turma.close()
else:
    print('Opcao invalida')