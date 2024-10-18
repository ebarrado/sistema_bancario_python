import textwrap

#criar funções
#separar as funções: sacar, depositar, visualizar historico
#criar duas funções criar usuario e criar conta corrente (vincular com usuario)

def menu():
    menu = """\n
    =======================INICIO MENU =======================
    [0]\tSair    
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Conta
    [6]\tNovo Usuário
    
    =========================FIM MENU ========================
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor: 2f}\n"
        print("\n===Deposito realizado com sucesso! ===")
    else:
        print("\n---Operação falhou! O valor informado é invalido---")
    
    return saldo, extrato
#nomeada
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= limite_saques

            if excedeu_saldo:
                print("----Operação falhou! Você não tem saldo----")
                print(f"\nSeu saldo atual está em: R$ {saldo: .2f}")

            elif excedeu_limite:
                print("----A Operação falhou! O valor do saque excede o limite---")
            elif excedeu_saques:
                print("----Operação falhou! Número máximo de saques execido---")
                

            if valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor: 2f}\n"
                numero_saques += 1
                print("\n===Saque realizado com Sucesso===")
            else:
                print("---Operação falhou! O valor informado é invalido---")
                
            return saldo, extrato
                
#posicional e nomeada                
def exibir_extrato(saldo, /, *, extrato):
    print("Opção Extrato selecionada")
    print("\n=======================EXTRATO BANCÁRIO=======================\n")
    print(f"\nSaldo: R$ {saldo: .2f}")
    print("==============================================================\n")
    
    return saldo, extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n--Já existe usuario com esse CPF!---")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado)")
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})
    
    print("===Usuário criado com sucesso===")
    
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] ==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
      
        opcao= menu()
        
        if opcao == '1':
            print("Opção depositar selecionada")
            valor = float(input("Informe o valor do deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
           
        elif opcao == '2':
            print('Opção sacar selecionada')
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
           
        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
            
       
            
      
            
        elif opcao == '6':
            criar_usuario(usuarios)
            
            
        elif opcao =='0':
            break
            print("Saindo do Sistema ...")
            
        else:
            print("Opção inválida, tente novamente")
            
main()