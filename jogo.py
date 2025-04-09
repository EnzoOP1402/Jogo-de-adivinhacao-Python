import os
from random import randint

jogar = 1

while jogar == 1:
    numGerado = randint(1000,9999)
    
    milhar = numGerado // 1000
    centena = (numGerado % 1000) // 100
    dezena = (numGerado % 100) // 10
    unidade = numGerado % 10

    cont = 1
    venceu = 0
    acertos = 0
    pos1 = pos2 = pos3 = pos4 = -1
    dica1 = dica2 = dica3 = dica4 = 0
    tipo1 = tipo2 = tipo3 = tipo4 = 0
   
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\n\t=-=-=-=-= BEM VINDO(A) AO JOGO SECRETO =-=-=-=-=\n\n')
    print('Você tem 10 tentativas para acertar o número secreto entre [1000 e 9999]\n')
    print('Caso você acerte a posição e o número, o jogo irá mantê-lo e informará que está correto!\n')
    print('A partir da 5ª tentativa, o jogo irá te ajudar com dicas.\n\tBoa sorte!!')
    input('\n\t<< Tecle Enter para continuar >>')

    os.system('cls' if os.name == 'nt' else 'clear')
                                  
    while cont <= 10:
        print('-'*50)
        numPalpite = int(input(f"\n\t>> {cont}ª Tentativa <<\nDigite seu palpite: "))
        while numPalpite < 1000 or numPalpite > 9999:
            numPalpite = int(input(f"\nTentativa inválida. O número deve ser entre 1000 e 9999.\n\n\t>> {cont}ª Tentativa <<\nDigite seu palpite: "))

        if numPalpite == numGerado:
            venceu = 1
            break  

        milhar2 = numPalpite // 1000
        centena2 = (numPalpite % 1000) // 100
        dezena2 = (numPalpite % 100) // 10
        unidade2 = numPalpite % 10

        if -3 <= pos1 < 0 and milhar == milhar2:
            pos1 = milhar2
            acertos += 1
        if -3 <= pos2 < 0 and centena == centena2:
            pos2 = centena2
            acertos += 1
        if -3 <= pos3 < 0 and dezena == dezena2:
            pos3 = dezena2
            acertos += 1
        if -3 <= pos4 < 0 and unidade == unidade2:
            pos4 = unidade2
            acertos += 1

        print(f'\nVocê acertou {acertos} dígito(s) dessa vez...')
        print('\nSeu código atual é: ', end='')
        if -3 <= pos1 < 0:
            print('__', end=' ')
        else:
            print(pos1, end=' ')
        if -3 <= pos2 < 0:
            print('__', end=' ')
        else:
            print(pos2, end=' ')
        if -3 <= pos3 < 0:
            print('__', end=' ')
        else:
            print(pos3, end=' ')
        if -3 <= pos4 < 0:
            print('__', end=' ')
        else:
            print(pos4, end=' ')

        if cont < 10:
            print(f'\n\nFalta(m) {10-cont} tentativa(s)...\n')

        acertos = 0

        if (5 <= cont < 10) and not ((pos1 > -1 or pos1 < -2) and (pos2 > -1 or pos2 < -2) and (pos3 > -1 or pos3 < -2) and (pos4 > -1 or pos4 < -2)):
            print(f'\nVou te dar uma dica...\n')
            dica = randint(1,4)

            while dica < 5:
                if (dica == 1 and (pos1 > -1 or pos1 < -2)) or (dica == 2 and (pos2 > -1 or pos2 < -2)) or (dica == 3 and (pos3 > -1 or pos3 < -2)) or (dica == 4 and (pos4 > -1 or pos4 < -2)):
                    dica = randint(1,4)
                else:
                    break

            if dica == 1:
                tipo = randint(1,2)

                while tipo < 3:
                    if (tipo == tipo1 == 1) or (tipo == tipo1 == 2):
                        tipo = randint(1,2)
                    else:
                        break

                if tipo == 1:
                    if milhar % 2 == 0:
                        print('==> O Primeiro dígito (milhar) é PAR!!\n')
                        dica1 = 1
                        pos1 -= 1
                        tipo1 = 1
                    else:
                        print('==> O Primeiro dígito (milhar) é ÍMPAR!!')
                        dica1 = 2
                        pos1 -= 1
                        tipo1 = 1

                else:
                    if milhar >= 5:
                        print('==> O Primeiro dígito (milhar) é MAIOR OU IGUAL A 5!!')
                        dica1 = 3
                        pos1 -= 1
                        tipo1 = 2
                    else:
                        print('==> O Primeiro dígito (milhar) é MENOR QUE 5!!')
                        dica1 = 4
                        pos1 -= 1
                        tipo1 = 2

            elif dica == 2: 
                tipo = randint(1, 2)
                
                while tipo < 3:
                    if (tipo == tipo2 == 1) or (tipo == tipo2 == 2):
                        tipo = randint(1,2)
                    else:
                        break

                if tipo == 1:
                    if centena % 2 == 0:
                        print('==> O Segundo dígito (centena) é PAR!!')
                        dica2 = 1
                        pos2 -= 1
                        tipo2 = 1
                    else:
                        print('==> O Segundo dígito (centena) é ÍMPAR!! ')
                        dica2 = 2
                        pos2 -= 1
                        tipo2 = 1
                else:
                    if centena >= 5:
                        print('==> O Segundo dígito (centena) é maior ou igual a 5!!')
                        dica2 = 3
                        pos2 -= 1
                        tipo2 = 2
                    else:
                        print('==> O Segundo dígito (centena) é menor que 5!!')
                        dica2 = 4
                        pos2 -= 1
                        tipo2 = 2

            elif dica == 3:
                tipo = randint(1,2)

                while tipo < 3:
                    if (tipo == tipo3 == 1) or (tipo == tipo3 == 2):
                        tipo = randint(1,2)
                    else:
                        break

                if tipo == 1:
                    if dezena % 2 == 0:
                        print('==> O terceiro dígito (dezena) é PAR!!')
                        dica3 = 1
                        pos3 -= 1
                        tipo3 = 1
                    else:
                        print('==> O terceiro dígito (dezena) é ÍMPAR!!')
                        dica3 = 2
                        pos3 -= 1
                        tipo3 = 1
                else:
                    if dezena >= 5:
                        print('==> O terceiro dígito (dezena) é MAIOR OU IGUAL A 5!!')
                        dica3 = 3
                        pos3 -= 1
                        tipo3 = 2
                    else:
                        print('==> O terceiro dígito (dezena) é MENOR QUE 5!!')
                        dica3 = 4
                        pos3 -= 1
                        tipo3 = 2

            elif dica == 4: 
                tipo = randint(1, 2)
                
                while tipo < 3:
                    if (tipo == tipo4 == 1) or (tipo == tipo4 == 2):
                        tipo = randint(1,2)
                    else:
                        break

                if tipo == 1:
                    if unidade % 2 == 0:
                        print('==> O Quarto dígito (unidade) é PAR!!')
                        dica4 = 1
                        pos4 -= 1
                        tipo4 = 1
                    else:
                        print('==> O Quarto dígito (unidade) é ÍMPAR!! ')
                        dica4 = 2
                        pos4 -= 1
                        tipo4 = 1
                else:
                    if unidade >= 5:
                        print('==> O Quarto dígito (unidade) é maior ou igual a 5!!')
                        dica4 = 3
                        pos4 -= 1
                        tipo4 = 2
                    else:
                        print('==> O Quarto dígito (unidade) é menor que 5!!')
                        dica4 = 4
                        pos4 -= 1
                        tipo4 = 2    
            
            print('\n==> ', end='')
            if -3 <= pos1 < 0:
                if pos1 == -1 or tipo1 == 0 or dica1 == 0:
                    print('__', end=' ')
                else:
                    if dica1 == 1:
                        print('PAR', end=' ')
                    elif dica1 == 2:
                        print('ÍMPAR', end=' ')
                    elif dica1 == 3:
                        print('>=5', end=' ')
                    elif dica1 == 4:
                        print('<5', end=' ')
            else:
                print(pos1, end=' ')
            if -3 <= pos2 < 0:
                if pos2 == -1 or tipo2 == 0 or dica2 == 0:
                    print('__', end=' ')
                else:
                    if dica2 == 1:
                        print('PAR', end=' ')
                    elif dica2 == 2:
                        print('ÍMPAR', end=' ')
                    elif dica2 == 3:
                        print('>=5', end=' ')
                    elif dica2 == 4:
                        print('<5', end=' ')
            else:
                print(pos2, end=' ')
            if -3 <= pos3 < 0:
                if pos3 == -1 or tipo3 == 0 or dica3 == 0:
                    print('__', end=' ')
                else:
                    if dica3 == 1:
                        print('PAR', end=' ')
                    elif dica3 == 2:
                        print('ÍMPAR', end=' ')
                    elif dica3 == 3:
                        print('>=5', end=' ')
                    elif dica3 == 4:
                        print('<5', end=' ')
            else:
                print(pos3, end=' ')
            if -3 <= pos4 < 0:
                if pos4 == -1 or tipo4 == 0 or dica4 == 0:
                    print('__', end=' ')
                else:
                    if dica4 == 1:
                        print('PAR', end=' ')
                    elif dica4 == 2:
                        print('ÍMPAR', end=' ')
                    elif dica4 == 3:
                        print('>=5', end=' ')
                    elif dica4 == 4:
                        print('<5', end=' ')
            else:
                print(pos4, end=' ')
            print('\n')

        cont += 1

    if venceu == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n\t>=<>=<>=< PARABÉNS >=<>=<>=<\nVocê acertou o <<CÓDIGO SECRETO>> na {cont}ª tentativa.')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\nQue pena! Não foi dessa vez :(\nO <<CÓDIGO SECRETO>> era {numGerado}\nMas não se preocupe, você pode jogar de novo!\n')

    print('-' * 60)
    
    jogar = int(input('\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÃO\n\n>> '))
    while jogar not in [0, 1]:
        jogar = int(input('\nOpção inválida\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÃO\n\n>> '))  

print('\n\t=-=-=-=-= Muito obrigado por jogar!! =-=-=-=-=')