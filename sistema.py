#sistema Python com operações básicas: sacar, depositar e visualizar extrato
#Operações: deposito, saque e extrato
#deposito valores positivos
#1 usuário
#todos depositos devem ser armazenados em uma variável e exibidos na operação de extrato
#sistema realize 3 saques diarios limite máximo 500,00 por saque
#sem saldo: mensagem "Nâo é possível realiar saque, conta sem saldo"
#todos saques devem ser armazenados em uma variável e exibidos na operação de extrato
#extrato deve listar todos os depósitos e saques realizados na conta. 
#no fim deve ser exibido o saldo atual da conta
# valores exibidos utilizando o formato R$ xxx.xx 1500.45 = R$ 1500.45

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def menu():
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUES
    while True:
        print('''
        [1]Depositar
        [2]Sacar
        [3]Extrato
        [4]Sair
        ''')

        opcao= input('Digite uma opção: ')

        if opcao == '1':
            print("Opção depositar selecionada")
            valor = float(input("Informe o valor do deposito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Deposito: R$ {valor: 2f}\n"
            else:
                print("Operação falhou! O valor informado é invalido")
        elif opcao == '2':
            print('Opção sacar selecionada')
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo")
                print(f"\nSeu saldo atual estaá em: R$ {saldo: .2f}")

            elif excedeu_limite:
                print("A Operação falhou! O valor do saque excede o limite")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques execido")
                

            if valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor: 2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é invalido")
        elif opcao == '3':
            print("Opção Extrato selecionada")
            print("\n=======================EXTRATO BANCÁRIO=======================\n")
            print(f"\nSaldo: R$ {saldo: .2f}")
            print("==============================================================\n")
        elif opcao =='4':
            break
            print("Saindo do Sistema ...")
        else:
            print("Opção inválida, tente novamente")


menu()