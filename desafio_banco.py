# Sistema simples de conta bancaria de um usuário


saldo = 0

limite = 500

extrato = ""

numero_saques = 0

LIMITE_SAQUES = 3

numero_operacao = 0

while True:

    print("\nFavor escolher qual atividade bancária a ser feita\n")

    print("[1] - Depósito")

    print("[2] - Saque")

    print("[3] - Extrato")

    print("[4] - Sair")

    opcao = input("\nAção: ")

    if opcao == "1":

        processo_depositoPositivo = 0

        while processo_depositoPositivo == 0:

            valor_deposito = int(input("Inserir o valor a ser depositado: "))

            if valor_deposito <= 0:

                print("O valor do depósito não pode ser negativo ou zero\n")

            else:

                processo_depositoPositivo = 1

        print("O depósito no valor de R$", valor_deposito, "foi efetivado com sucesso")

        saldo += valor_deposito

        print("Saldo total: R$", saldo, "\n")

        numero_operacao += 1

        extrato += f"Número da operação: {numero_operacao}\nTipo de operação: Depósito.\nValor do Depósito: R$ {valor_deposito}\n---------------------------\n"



    elif opcao == "2":

        if numero_saques == LIMITE_SAQUES:

            print("Já atingiu o limite de saques diário\n")

        else:

            processo_saquePositivo = 0

            while processo_saquePositivo == 0:

                valor_saque = int(input("Inserir o valor a ser sacado: "))

                if valor_saque <= 0:

                    print("O valor do saque não pode ser negativo ou zero\n")

                else:

                    processo_saquePositivo = 1

            if valor_saque > saldo:

                print("O valor a ser sacado é maior que o saldo da conta\n")

            elif valor_saque > limite:

                print("O valor a ser sacado é maior que o limite estabelecido de saque de R$", limite, "\n")

            else:

                print("O saque no valor de R$", valor_saque, "foi efetivado com sucesso")

                saldo -= valor_saque

                print("Saldo total: R$", saldo, "\n")

                numero_saques += 1

                numero_operacao += 1

                extrato += f"Número da operação: {numero_operacao}\nTipo de operação: Saque.\nValor do Saque: R$ {valor_saque}\n---------------------------\n"



    elif opcao == "3":

        print(extrato)

        print("Saldo total: R$", saldo, "\n")



    elif opcao == "4":

        print("\nObrigado por utilizar nosso sistema!")

        break



    else:

        print("Operação inválida\n")