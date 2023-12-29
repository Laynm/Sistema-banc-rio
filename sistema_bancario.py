menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            print("Valor depositado com sucesso!!!")
            extrato += f"Depósito realizado: R$ {valor_deposito:.2F}\n"
        else:
            print("Valor inválido, por favor tente novamente.")

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite_diario
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor_saque > 0 and not excedeu_saldo and not excedeu_limite and not excedeu_saques:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2F}\n"
            numero_saques += 1
        elif excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente!")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite diário de saques")
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o limite de saques")
        else:
            print("Operação falhou! O valor informado é inválido, por favor tente novamente.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n========== EXTRATO ==========")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print(f"Opção inválida ({opcao}), por favor selecione novamente a operação desejada.")
