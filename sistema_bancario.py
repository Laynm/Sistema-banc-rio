menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
       print("Deposito")
    
    if opcao == "s":
        print("Saque")
    
    if opcao == "e":
        print("Extrato")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
    