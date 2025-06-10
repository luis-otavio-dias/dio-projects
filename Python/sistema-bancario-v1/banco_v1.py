saldo = 0
saques = 0
extrato = []


menu = """
Opções:
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
"""

print(menu)

while True:
    opcao = input("Escolha uma opção: ")
    if opcao not in "123":
        print("Opção inválida. Tente novamente.")

    if opcao == "1":
        print("Depósito")
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")

    if opcao == "2":
        print("Saque")
        print(saques)
        if saldo == 0:
            print("Sem saldo. Saque indisponível.")
        elif saques != 3:

            valor = float(input("Digite o valor do saque: "))

            if valor > 500:
                print("Valor ultrapassa o máximo permitido de R$500.00.")
            if valor > saldo:
                print(f"Valor ultrapassa o saldo R${saldo:.2f}.")

            saldo -= valor
            saques += 1
            extrato.append(f"Saque: R${valor:.2f}")
        else:
            print("Limite diário de saque atingido.")

    if opcao == "3":
        print("Extrato")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for i in extrato:
                print(i)
            print(f"Saldo atual: R${saldo:.2f}")

    if opcao == "4":
        print("Encerrando...")
        saques = 0
        break
