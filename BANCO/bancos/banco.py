def saque(valor):
    global saldo
    global numero_saques
    if saldo > valor and valor > 0:
        saldo = saldo - valor
        return print(f"seu saldo agora é de {saldo}")
    elif saldo < valor:
        return print("operação invalida: Saldo insuficiente")
    elif (valor < 0):
        return print("Operação invalida: Numero inserido nao valido")
def deposito(valor):
    global saldo
    if(valor>0):
        saldo = saldo + valor
        return print(f"seu saldo agora é de {saldo}")
    elif(valor<0):
        return print("Operação invalida: Valor de deposito negativo")

menu = """
[s] = saque;
[d] = deposito;
[e] = extrato;
[q] = sair;
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 's':
        if (LIMITE_SAQUES <= 0):
            print("limite de saques atingido nao podera mais efetuar saques")
        else:
            valor = float(input("Digite o Valor"))
            saque(valor)
            extrato += f"Saque: R$ {valor: }\n"
            numero_saques = numero_saques + 1
            LIMITE_SAQUES = LIMITE_SAQUES - 1
    elif opcao == 'd':
        valor = float(input('Digite o valor'))
        deposito(valor)
        extrato += f"Deposito: R$ {valor: }\n"
    elif opcao == 'e':
        print('===================EXTRATO=================')
        print('Nao foram realizadas movimentacoes' if not extrato else extrato)
        print(f'\nSaldo R$: {saldo}')
        print('===========================================')
    elif opcao == 'q':
        break
    else:
        print("opcao invalida")