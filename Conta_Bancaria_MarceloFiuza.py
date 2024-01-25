menu, saldo, deposito, transferencia, saldo = 0, 0, 0, 0, 0
while menu != 4: # O menu irá ficar em loop até que o usuário encerre a operação digitando a opçãp "4"
    print("Aplicação de Conta bancária Iniciada, escolha uma opção: ")
    menu = int(input("1 - Fazer um Depósito | 2 - Relizar uma Transferência | 3 - Mostrar Saldo | 4 - Encerrar a Operação: ")) # Opções de menu para o usuário escolher
    if menu == 1: # Primeira opção do menu, para fazer um depósito
        deposito = float(input("Informe o valor do Depósito: ")) # valor do depósito realizado pelo usuário
        if (deposito > 0): # irá realizar a operação de depósito somente para valores acima de 0
            saldo = saldo + deposito # somatório do valor atual mais o depósito realizado
            print("O depósito foi realizado com sucesso") # Mensagem informando que a operação ocorreu 
            print(f"O seu saldo atual é R${saldo:0.2f}") # Imprime o saldo após o depósito realizado
        else:
            print("O valor não é válido para um depósito, a operação não foi realizada") # Informa ao usuário que o valor informado para depósito não é válido
            print(f"O seu saldo atual é R${saldo:0.2f}") # Imprime o saldo atual
    elif menu == 2: # Segunda opção do menu, para fazer uma transferência
        transferencia = float(input("Informe o valor da transferência: ")) #valor da transferência realizada pelo usuário
        valor_minimo = 2 + transferencia # criado uma variável para considerar um valor mínimo possível em caso de transferência (valor da transferência + cobrança de R$2,00 pela operação)
        if (saldo > 0) and (saldo < 10000) and (saldo >= valor_minimo) and (transferencia > 0): #transferência possível somente para valores entre 0 e R$10000, considerando também o valor da taxa de transferência e a transferência sendo maior que zero
            saldo = saldo - transferencia - 2 # subtrai a transferência do saldo e desconta a taxa de R$2,00
            print(f"O seu saldo atual é R${saldo:.2f}") # Imprime o saldo atual
        elif (saldo > 0) and (saldo >= 10000) and (saldo > transferencia) and (transferencia > 0):
            saldo = saldo - transferencia # subtrai a transferência do valor do saldo
            print(f"O seu saldo atual é R${saldo:.2f}") # Imprime o saldo atual
        else:
            print("O valor informado não é válido para uma transferência, a operação não foi realizada")
            print(f"O seu saldo atual é R${saldo:.2f}")  # Imprime o saldo atual
    elif menu == 3: # terceira opção do menu, para mostrar o saldo do usuário
        print(f"O seu saldo atual é R${saldo:.2f}") # Informa ao usuário o saldo atual
    elif menu == 4: # caso o usuário não tenha mais interresse em fazer operações e opte por encerrar o programa
        print("Programa encerrado, agradecemos... ") # mensagem ao usuário que o programa foi finalizado 
    else:
        print("Não foi informado uma opção válida, tente novamente!") # caso o usuário digite um valor diferente das opções válidas no menu irá imprimir essa mensagem e voltar ao loop inicial do menu
