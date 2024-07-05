saldo = 0
extrato = ""
limite_diario_de_saque = 3

while True:
    print("\nESCOLHA A OPERAÇÃO\n")
    opcao = int(input("1 - Depósitar\n2 - Sacar\n3 - Saldo\n4 - Extrato\n5 - Sair\n"))
    
    if opcao == 1:
        deposito = float(input("\nDigíte o valor do depósito: "))
       
        if deposito > 0:
            saldo += deposito
            extrato += f"Depositou:     R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso.")
        else:
            print("\nERRO! Valor negativo ou nulo.\n")
    
    elif opcao == 2:
        if limite_diario_de_saque <= 3:
            saque = float(input("\nDigíte o valor de saque: "))

            if saque > 500 and saque < saldo:
                print("Não é permitido sacar valores maiores que R$ 500.00 em uma única operação")

            elif saque > saldo:
                print("\nVocê não possui saldo suficiente.")
           
            elif saque <= 0:
                print("\nERRO! Valor negativo ou nulo.")

            else:
                saldo -= saque
                print(f"Saque de R$ {saque:.2f} efetuado com sucesso.")
                saque *= -1
                extrato += f"Sacou:         R${saque:.2f}\n"
                limite_diario_de_saque += 1

        else:
            print("\nLimite diário de 3 saques atingido.\n")

    elif opcao == 3:
        print(f"\nSaldo:         R$ {saldo:.2f}")

    elif opcao == 4:
        print(f"\nEXTRATO\n{extrato}")
        print(f"Saldo:         R$ {saldo:.2f}")

    elif opcao == 5:
        print("\nEncerrando...\n")
        break

    else: 
        print("\nErro! Opção inválida. Tente novamente.\n")











