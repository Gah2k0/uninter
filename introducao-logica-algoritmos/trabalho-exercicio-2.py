print("Bem vindo a Sorveteria do Gabriel Francisco")
print("------------------------------------Cardápio---------------------------------------")
print("| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |")
print("|      1      |         R$ 6,00        |       R$ 7,00      |        R$ 8,00      |")
print("|      2      |         R$ 11,00       |       R$ 13,00     |        R$ 15,00     |")
print("|      3      |         R$ 15,00       |       R$ 18,00     |        R$ 21,00     |")
print("-----------------------------------------------------------------------------------")
precoTotal = 0
while True: #loop infinito se não tiver break
    saborDesejado = input("Entre com o sabor desejado (tr/es/pr): ")
    if(saborDesejado != "tr" and saborDesejado != "es" and saborDesejado != "pr"):
        print("Sabor de Sorvete Inválido")
        continue
    quantidadeBolasSorvete = input("Entre com o número de bolas de sorvete desejado (1/2/3): ")
    if(quantidadeBolasSorvete != "1" and quantidadeBolasSorvete != "2" and quantidadeBolasSorvete != "3"):
        print("Quantidade de Bolas de Sorvete Inválida")
        continue

    if(saborDesejado == "tr" and quantidadeBolasSorvete == "1"):
        precoTotal += 6
    elif(saborDesejado == "tr" and quantidadeBolasSorvete == "2"):
        precoTotal += 11
    elif(saborDesejado == "tr" and quantidadeBolasSorvete == "3"):
        precoTotal += 15

    if(saborDesejado == "pr" and quantidadeBolasSorvete == "1"):
        precoTotal += 7
    elif(saborDesejado == "pr" and quantidadeBolasSorvete == "2"):
        precoTotal += 13
    elif(saborDesejado == "pr" and quantidadeBolasSorvete == "3"):
        precoTotal += 18

    if(saborDesejado == "es" and quantidadeBolasSorvete == "1"):
        precoTotal += 8
    elif(saborDesejado == "es" and quantidadeBolasSorvete == "2"):
        precoTotal += 15
    elif(saborDesejado == "es" and quantidadeBolasSorvete == "3"):
        precoTotal += 21

    if input("Deseja mais algum sorvete (s/digite outra tecla)?: ") == "s":
        continue #volta para o inicio do loop
    else:
        print("O valor total a ser pago: R$%.2f" %precoTotal)
        break #encerra o loop