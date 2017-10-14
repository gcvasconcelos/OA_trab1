def troca_valores(array, i, j):
    array[i], array[j] = array[j], array[i]
def heapify(array, comeco, fim):
    esquerda = 2 * comeco  + 1
    direita = 2 * (comeco  + 1)
    maximo = comeco
    if esquerda < fim and array[comeco] < array[esquerda]:
        maximo = esquerda
    if direita < fim and array[maximo] < array[direita]:
        maximo = direita
    if maximo != comeco:
        troca_valores(array, comeco, maximo)  
        heapify(array, maximo, fim)
    return  
def heapsort(array):
    fim = len(array)
    comeco = fim // 2 - 1
    for i in range(comeco, -1, -1):
        heapify(array, i, fim)
    for i in range(fim-1, 0, -1):
        troca_valores(array, i, 0)
        heapify(array, 0, i)
    return

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
    heapsort(indices)
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

def printa_arquivo(arquivo):
    for linha in arquivo:
        print(linha)
    return

def adicionar_registro(arq_registros, arq_indices, registros, indices, novo_registro):
    
    return

print('\n\tMenu')
print('1.\tVisualizar arquivos')
print('2.\tIncluir registro')
print('3.\tExcluir registro')
print('4.\tAtualizar registro')
opcao_menu =  input()
if opcao_menu == 1:
    print('\n1\tArquivo de dados')
    print('2\tArquivo de indices primarios')
    print("3\tArquivo de indice secundario 'OP'")
    print("4\tArquivo de indice secundario 'TURMA'\n")
    escolha =  input()
    if escolha == 1:
        arquivo = open('benchmarks/lista1.txt', 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    elif escolha == 2:
        arquivo = open('indice_lista1.ind', 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    elif escolha == 3:
        arquivo = open('op_lista1.ind', 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    elif escolha == 4:
        arquivo = open('turma_lista1.ind', 'r')
        printa_arquivo(arquivo)
        arquivo.close()
    else:
        print('Opção inválida')
elif opcao_menu == 2:
    novo_registro = {}
    print('Digite a matricula:')
    novo_registro['matric'] = input()
    print('Digite o nome:')
    novo_registro['nome'] = input()
    print('Digite o OP:')
    novo_registro['op'] = input()
    print('Digite a curso:')
    novo_registro['curso'] = input()
    print('Digite a turma:')
    novo_registro['turma'] = input()
    arq_registros = open('lista1.txt', 'w')
    arq_indices = open('lista1.txt', 'w')
    adicionar_registro(arq_registros, arq_indices, registros, indices, novo_registro)  
