#O petshop opera da seguinte maneira:
#•	Para cães com peso menor que 3 kg o valor base é de 40 reais;
#•	Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
#•	Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;
#•	Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais;

#	Para cães com pelo curto (c) o multiplicador é 1;
#	Para cães com pelo médio (m) o multiplicador é 1.5;
#	Para cães com pelo longo (l) o multiplicador é 2;

#♦	Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
#♦	Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
#♦	Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
#♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;


#O valor final da conta é calculado da seguinte maneira:

#total = base * multiplicador + extra


print('Bem-vindo a petshop do Gabriel Francisco!')
def cachorro_peso():
    pesoCachorro = input('Entre com o peso do cachorro: ')
    try:
        if int(pesoCachorro) > 50:
            print('Não aceitamos cachorros tão grandes')
            return cachorro_peso()
        if int(pesoCachorro) < 3:
            return 40
        elif int(pesoCachorro) < 10:
            return 50
        elif int(pesoCachorro) < 30:
            return 60
        return 70
    except ValueError:
        if isinstance(pesoCachorro, str):
            print('Você digitou um valor não numérico, tente novamente')
            return cachorro_peso()  #recursão


def cachorro_pelo():
    peloCachorro = input('Entre com o tamanho do pelo do cachorro: '
                         '\n c - Pelo Curto'
                         '\n m - Pelo Médio'
                         '\n l - Pelo Longo'
                         '\n >> ')
    if peloCachorro == 'c':
        return 1
    elif peloCachorro == 'm':
        return 1.5
    elif peloCachorro == 'l':
        return 2
    else:
        print('Você digitou uma opção inválida, por favor tente novamente')
        return cachorro_pelo() #recursão


def cachorro_extra():
    extra = 0
    while True:
        adicional = input('Deseja adicionar mais algum serviço? '
                             '\n 1 - Corte de Unhas - R$ 10,00'
                             '\n 2 - Escovar os Dentes - R$ 12,00'
                             '\n 3 - Limpeza de Orelhas - R$ 15,00'
                             '\n 0 - Não desejo mais nada'
                             '\n >> ')
        if adicional == '1':
            extra += 10
        elif adicional == '2':
            extra += 12
        elif adicional == '3':
            extra += 15
        elif adicional == '0':
            break
        else:
            print('Você digitou uma opção inválida, por favor tente novamente')
    return extra


precoBase = cachorro_peso() #coletando o preco base

multiplicador = cachorro_pelo() #coletando o multiplicador com base no tamanho do pelo

cachorroExtra = cachorro_extra() #adicionando possiveis extras

precoTotal = (float(precoBase) * float(multiplicador)) + float(cachorroExtra)
print('Total a pagar(R$): %.2f (peso: %.2f * pelo: %.2f + adicional(is): %.2f)' %(float(precoTotal), float(precoBase), float(multiplicador), float(cachorroExtra)))