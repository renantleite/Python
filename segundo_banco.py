import re
#funcoes usadas
def formato_CPF(cpf):
    padrao = r'\d{3}\.\d{3}\.\d{3}\-\d{2}'
    if re.match(padrao,cpf):
        return True
    else:
        return False
def verificar_CPF(cpf,usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False
def saque(valor,cpf,usuarios):
    for usuario in usuarios:
        if(usuario['cpf'] == cpf):
            if usuario.get('numero_saques', 0) < 3:
                if usuario['saldo'] > valor and valor > 0:
                    usuario['saldo'] = usuario.get('saldo') - valor
                    usuario['numero_saques'] = usuario.get('numero_saques') + 1
                    usuario['extrato'] +=  f"Saque: R$ {valor:.2f}\n"
                    return print(f"você realizou um saque de R$: {valor}\nSeu saldo agora é de {usuario['saldo']}")
                elif saldo < valor:
                    return print("operação invalida: Saldo insuficiente")
                elif (valor < 0):
                    return print("Operação invalida: Numero inserido nao valido")
            else:
                print("numero de saques diarios limite alcancado")
def deposito(valor,cpf,usuarios):
    for usuario in usuarios:
        if(usuario['cpf'] == cpf):
            if(valor>0):
                usuario['saldo'] = usuario.get('saldo') + valor
                usuario['extrato'] = f"Depósito: R$ {valor:.2f}\n"
                return print(f"seu saldo agora é de {usuario['saldo']}")
            elif(valor<0):
                return print("Operação invalida: Valor de deposito negativo")
            else: 
                return print("Operação invalida: Valor de deposito nulo")
    print("Usuario nao encontrado")
def extrato_por_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            extrato_usuario = usuario.get('extrato', '')
            saldo_usuario = usuario.get('saldo', 0)
            print('===================EXTRATO=================')
            print('Nao foram realizadas movimentacoes' if  not extrato_usuario else extrato_usuario)
            print(f'\nSaldo R$: {saldo_usuario}')
            print('===========================================')
            return
    print("CPF não encontrado.")
#variaveis usadas
menu = """
[s] = saque;
[d] = deposito;
[e] = extrato;
[c] = criar Usuario
[l] = listar usuarios
[q] = sair;
=> """
usuario = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
#menu no while
while True:
    opcao = input(menu)
    if opcao == 's':
        cpf = input("Digite o cpf\n: ")
        valor = float(input("Digite o Valor"))
        saque(valor,cpf,usuario)
    elif opcao == 'c':
        nomes = input('Qual o nome do usuário?\n: ')
        if (not nomes.isalpha()):
            print("ERRO: Nao aceitamos numeros")
        else:
            cpf = (input('Qual o seu CPF digite no formato XXX.XXX.XXX-XX?\n: '))
            if(formato_CPF(cpf)):
                if not verificar_CPF(cpf, usuario):
                    usuario.append({'nome': nomes, 'cpf': cpf, 'saldo': 0,'extrato':extrato,'numero_saques':0})
                    print(f"Usuário {nomes} cadastrado.")
                else:
                    print("CPF ja cadastrado")
            else:
                print(f'formato errado do CPF')
    elif opcao == 'd':
        cpf = input("Digite o cpf\n: ")
        valor = float(input('Digite o valor'))
        deposito(valor,cpf,usuario)
    elif opcao == 'l':
        print(f'Usuarios Cadastrados:')
        for user in usuario:
            print(user['nome'])
    elif opcao == 'e':
        cpf = input('Digite seu cpf\n: ')
        extrato_por_cpf(cpf,usuario)
    elif opcao == 'q':
        break
    else:
        print("opcao invalida")