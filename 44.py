valor = float(input('Qual o valor do produto a ser pago? '))
pagamento = int(input('Deseja pagar à vista ou parcelado? \nDigite 1 para à vista \nDigite 2 para parcelado \n'))
if pagamento == 1:
    print('Oba! o pagamento à vista tem desconto. \nNo dinheiro o desconto é de 10%. \nNo cartão de débito o desconto é de 5%.')
    vista = int(input('Qual a forma de pagamento que deseja realizar? \nDigite 1 para à vista em dinheiro. \nDigite 2 para à vista no cartão de débito. \n'))
    if vista == 1:
        desconto = valor * 0.1
    elif vista == 2:
        desconto = valor * 0.05
    elif vista != 1 and vista != 2:
        print('Opção inválida. \nVolte ao início e refaça todos os passos.')
    print('O valor do produto é R$ {:.2f}. \nO desconto vai ser no valor de R$ {:.2f}. \nO valor final do produto vai ser R$ {:.2f}'.format(valor, desconto, valor - desconto))
elif pagamento == 2:
    print('Em até 2x no cartão de crédito não tem juros. Acima disso o juros é de 20%.')
    parcelas = int(input('Digite o número de parcelas que deseja para pagar: '))
    if parcelas <= 2:
        print('Nessa condição de pagamento não há juros e o valor será pago em {} parcela(s) de R$ {:.2f}'.format(parcelas, valor / parcelas))
    else:
        juros = valor * 0.2
        print('Nessa condição de pagamento há juros, o que implica no acréscimo de 20% do valor da compra.')
        print("""Dessa forma, com o acréscimo de R$ {:.2f} na compra, o valor final do produto fica R$ {:.2f}
O valor será pago em {} parcelas de R$ {:.2f}. """.format(juros, valor + juros, parcelas, (valor + juros) / parcelas))
else:
    print('Opção inválida. \nTente novamente...')

#Deu trabalho esse aqui...