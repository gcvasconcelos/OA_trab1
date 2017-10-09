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

def cria_indices(indices, arquivo):
	arquivo.seek(0,0)
	referencia = 0
	for linha in arquivo:
		dados = linha.split()
		nome = ' '.join(dados[1:-3])
		matricula = dados[0]
		chave_primaria = matricula + '$' + nome
		indices.write(chave_primaria[0:30] + '\t' + str(referencia) + '\n')
		print(chave_primaria[0:30] + '\t' + str(referencia) + '\n')
		referencia += 1
	return

def printa_indices(indices):
	print('CP\t\t\t\tREF')
	for linha in indices:
		print linha
	return

def cria_indices_secundarios(op, turma, primario, dados):
	for i in range(len(dados)):
		op.write(dados[i][-1] + '\n')
		turma.write(dados[i][-3] + '\n')
	return


lista1 = open('benchmarks/lista1.txt', 'r')
dados_arquivo = printa_arquivo(lista1)
indices1 = open('indice_lista1.ind', 'w+')
cria_indices(indices1, lista1)
# printa_indices(indices1)
secundario_op = open('op_lista1.ind', 'w+')
secundario_turma = open('turma_lista1.ind', 'w+')
cria_indices_secundarios(secundario_op, secundario_turma, indices1, dados_arquivo)

lista1.close()
indices1.close()