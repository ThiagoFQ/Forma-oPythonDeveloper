menu = '''

[1] Depósito
[2] Extrato
[3] Saque
[0] Sair

Informe sua solicitação: '''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    solicitacao = int(input(menu))

    if solicitacao == 1:
        valor = float(input(f'Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Verifique seu depósito! O valor informado não é válido. Operação cancelada.')

    elif solicitacao == 2:
        print('\n========== EXTRATO ==========')
        print('Não forma realizadas movimentações no período.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=============================')

    elif solicitacao == 3:
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Operação cancelada! Saldo insuficiente.')

        elif excedeu_limite:
            print('Operação cancelada! O valor do saque excede o limte disponível.')

        elif excedeu_saque:
            print('Operação cancelada! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque:    R$ {valor:.2f}\n'
            numero_saque += 1

        else:
            print('Operação cancelada! Valor informado não é válido.')

    elif solicitacao == 0:
        print('Obrigado por usar nossos serviços.')
        break

    else:
        print('Opção inválida! Favor escolher uma opção.')

