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

def cadastrar_colaborador(id):
    nome = input('Informe o nome do novo colaborador: ')
    setor = input('Informe o setor do novo colaborador: ')
    pagamento = input('Informe o valor de pagamento do novo colaborador (R$): ')

    colaborador = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'pagamento': pagamento
    }
    lista_colaboradores.append(colaborador)

cadastrar_colaborador(1)
print(lista_colaboradores)