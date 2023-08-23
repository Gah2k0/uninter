# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

#numeros = (10, 15, 20, 25, 30)
#for numero in numeros:
   #print(numero)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#for i in range (7, 26, 3):
  # print(i)

#i = 100
#while (i <= 999):
   #print(i)
   #i += 10


print('Bem vindo a loja do Gabriel Francisco')
valorProduto = input('Entre com o valor do produto: ')
quantidadeProduto = input('Entre com a quantidade do produto: ')

quantidadeProduto = float(quantidadeProduto) #convertendo tipo string para float
valorProduto = float(valorProduto) #convertendo tipo string para float
desconto = 0 #definindo variavel em escopo global

if(quantidadeProduto >= 2000):
   desconto = 0.15 * valorProduto
elif(quantidadeProduto >= 1000):
   desconto = 0.10 * valorProduto
elif(quantidadeProduto >= 200):
   desconto = 0.05 * valorProduto
else:
   desconto = 0 * valorProduto

print("O valor SEM desconto: R$ %.2f" % (valorProduto * quantidadeProduto))
print("O valor COM desconto: R$ %.2f" % ((valorProduto - desconto) * quantidadeProduto))