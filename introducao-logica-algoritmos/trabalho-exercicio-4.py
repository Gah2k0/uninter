#1)	Cadastrar Colaborador
#2)	Consultar Colaborador
    #1.	Consultar Todos
    #2.	Consultar por Id;
    #3.	Consultar por Setor;
    #4.	Retornar ao menu;
#3)	Remover Colaborador
#4)	Encerrar Programa



lista_colaboradores = []
id_global = 0

def formatar_print(colaborador):
    print('\nDados do Colaborador: \n'
          'ID: %s \n'
          'NOME: %s \n'
          'SETOR: %s \n'
          'REMUNERAÇÃO: R$ %s \n' %(colaborador['id'], colaborador['nome'], colaborador['setor'], colaborador['pagamento']))


def cadastrar_colaborador(id):
    print("--------------------------------MENU DE CADASTRO-----------------------------------")
    nome = input('Informe o nome do novo colaborador: ')
    setor = input('Informe o setor do novo colaborador: ')
    pagamento = input('Informe o valor de pagamento do novo colaborador (R$): ')
    print("-----------------------------------------------------------------------------------")
    print("***********************************************************************************")

    colaborador = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'pagamento': pagamento
    }
    lista_colaboradores.append(colaborador)
    formatar_print(colaborador)
    global id_global
    id_global += 1

def consultar_colaborador():
    print("---------------------------------MENU DE CONSULTA----------------------------------")
    opcao = input('Escolha a opção desejada: \n'
          '1. Consultar todos\n'
          '2. Consultar por Id\n'
          '3. Consultar por Setor\n'
          '4. Retornar ao menu principal\n'
          '>> ')
    if opcao == '1':
        for colaborador in lista_colaboradores:
            formatar_print(colaborador)
    elif opcao == '2':
        id = input('por favor digite o Id do colaborador: ')
        formatar_print(lista_colaboradores[int(id)])
    elif opcao == '3':
        setor = input('por favor digite o setor desejado: ')
        for colaborador in lista_colaboradores:
            if colaborador.get('setor') == setor:
                formatar_print(colaborador)

def remover_colaborador():
    print("---------------------------MENU DE REMOÇÃO DE COLABORADOR--------------------------")
    id = input('por favor digite o Id do colaborador que deseja remover: ')
    try:
        lista_colaboradores.pop(int(id))
        print('Colaborador removido com sucesso.')
    except IndexError:
        print('Desculpe, esse Id é inválido, tente novamente')


#cadastrar_colaborador(1)
#print(lista_colaboradores)

print("Bem-vindo ao Sistema de Gestão de Colaboradores de Gabriel Francisco")
while(True):
    print("---------------------------------MENU PRINCIPAL------------------------------------")
    opcao = input('O que você deseja fazer: \n'
          '1. Cadastrar Colaborador\n'
          '2. Consultar Colaborador\n'
          '3. Remover um Colaborador\n'
          '4. Sair\n'
          '>> ')
    print("-----------------------------------------------------------------------------------")
    print("***********************************************************************************")

    if opcao == '1':
        cadastrar_colaborador(id_global)
    elif opcao == '2':
        try:
            consultar_colaborador()
        except IndexError:
            print('Desculpe, esse Id é inválido, tente novamente')
    elif opcao == '3':
        remover_colaborador()
    elif opcao == '4':
        print('Obrigado por usar o Sistema de Gestão de Colaboradores de Gabriel Francisco, volte sempre!')
        break
    else:
        print('Opção inválida! Tente novamente.')
        continue