import os
from random import randint

# Loop principal do jogo
jogar = 1

while jogar == 1:
    # Gerando o número secreto
    # numGerado = randint(1000,9999)

    # Número secreto fixos
    numGerado = 1234
    
    # Desmembramento do número gerado
    milhar = numGerado // 1000
    centena = (numGerado % 1000) // 100
    dezena = (numGerado % 100) // 10
    unidade = numGerado % 10

    # Resetando variáveis para uma nova rodada
    cont = 1
    venceu = 0
    acertos = 0
    pos1 = pos2 = pos3 = pos4 = -1
    tipo1 = tipo2 = tipo3 = tipo4 = 0
   
    # Introdução do jogo
    print('\n\t=-=-=-=-= BEM VINDO(A) AO JOGO SECRETO =-=-=-=-=\n\n')
    print('Você tem 10 tentativas para acertar o número secreto entre [1000 e 9999]\n')
    print("Caso você acerte a posição e o número o jogo irá manter ele e informar que está correto!")
    print('A partir da 5ª tentativa, o jogo irá te ajudar com dicas.\n\tBoa sorte!!')
    input('\n\t<< Tecle Enter para continuar >>')

    # print('-' * 60)
    os.system('cls' if os.name == 'nt' else 'clear')
                                  
    # Loop de tentativas
    while cont <= 10:
        # Entrada do palpite do usuário
        numPalpite = int(input(f"\n\t>> {cont}ª Tentativa <<\nDigite seu palpite: "))
        while numPalpite < 1000 or numPalpite > 9999:
            numPalpite = int(input(f"\nTentativa inválida. O número deve ser entre 1000 e 9999.\n\t>> {cont}ª Tentativa <<\nDigite seu palpite: "))

        # Verificação de vitória
        if numPalpite == numGerado:
            venceu = 1
            break  # Sai do loop, pois o jogador venceu

        # Se não venceu, verifica os acertos

        # Desmembramento do número inserido
        milhar2 = numPalpite // 1000
        centena2 = (numPalpite % 1000) // 100
        dezena2 = (numPalpite % 100) // 10
        unidade2 = numPalpite % 10


        # Comparação dos dígitos
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
            
        # Exibição do resultado da tentativa
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

        print(f'\nFaltam {10-cont} tentativas...')

        # Zera a quantidade de acertos
        acertos = 0

        # >> DICAS <<
        # dicas do programa (se é par ou ímpar e/ou maior ou igual a cinco ou menor que cinco)
        if cont >= 5:
            print(f'\nVou te dar uma dica:\n')
            # Gera um número aleatório entre 1 e 4 -> DEFINE PARA QUAL POSIÇÃO A DICA VAI
            dica = randint(1,4)
            while dica < 5:
                if dica == 1 and -3 < pos1 < 0:
                    break
                if dica == 2 and -3 < pos2 < 0:
                    break
                
            if dica == 1:
                # Posição do milhar
                # Verificação do intervalo para evitar a repetição de dicas
                if -3 < pos1 < 0:
                    # Determina o tipo de dica
                    tipo = randint(1,2)
                    print(f'\nTipo: {tipo}\n')
                    # dica de par ou ímpar
                    if tipo == 1 and tipo1 != 1:
                        # Identifica se é par e mostra para o usuário
                        if milhar % 2 == 0:
                            print('==> O Primeiro dígito (milhar) é PAR!!')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos1 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo1 = 1
                        #caso não seja --> mostra para o usuário que é ímpar
                        else:
                            print('==> O Primeiro dígito (milhar) é ÍMPAR!!')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos1 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo1 = 1
                    # Dica do número ser maior ou igual a cinco ou número menor que cinco
                    else:
                        if tipo1 != 2:
                            #se o milhar for maior ou igual a cinco
                            if milhar >= 5:
                                print('==> O Primeiro dígito (milhar) é MAIOR OU IGUAL A 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos1 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo1 = 2
                            #se o milhar for menor que cinco
                            else:
                                print('==> O Primeiro dígito (milhar) é MENOR QUE 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos1 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo1 = 2

            elif dica == 2: 
                # Posição da centena
                # Verificação do intervalo para evitar a repetição de dicas
                if -3 < pos2 < 0:
                    tipo = randint(1, 2)
                    print(f'\nTipo: {tipo}\n')
                    if tipo == 1 and tipo2 != 1:
                        #identifica se é par e mostra para o usuário
                        if centena % 2 == 0:
                            print('==> O Segundo dígito (centena) é PAR!!')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos2 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo2 = 1
                        #caso não for --> mostra para o usuário que é ímpar
                        else:
                            print('==> O Segundo dígito (centena) é ÍMPAR!! ')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos2 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo2 = 1
                    #dica do número ser maior ou igual a cinco ou número menor que cinco
                    else:
                        if tipo2 != 2:
                            #se a dezena for maior ou igual a cinco
                            if centena >= 5:
                                print('==> O Segundo dígito (centena) é maior ou igual a 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos2 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo2 = 2
                            #se a dezena for menor que cinco
                            else:
                                print('==> O Segundo dígito (centena) é menor que 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos2 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo2 = 2

            elif dica == 3:
                # Posição da dezena
                # Verificação do intervalo para evitar a repetição de dicas
                if -3 < pos3 < 0:
                    # Determina o tipo de dica
                    tipo = randint(1,2)
                    print(f'\nTipo: {tipo}\n')
                    # dica de par ou ímpar
                    if tipo == 1 and tipo3 != 1:
                        #identifica se é par e mostra para o usuário
                        if dezena % 2 == 0:
                            print('==> O terceiro dígito (dezena) é PAR!!')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos3 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo3 = 1
                        #caso não for --> mostra para o usuário que é ímpar
                        else:
                            print('==> O terceiro dígito (dezena) é ÍMPAR!!')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos3 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo3 = 1
                    #dica do número ser maior ou igual a cinco ou número menor que cinco
                    else:
                        if tipo3 != 2:
                            #se a dezena for maior ou igual a cinco
                            if dezena >= 5:
                                print('==> O terceiro dígito (dezena) é MAIOR OU IGUAL A 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos3 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo3 = 2
                            #se a dezena for menor que cinco
                            else:
                                print('==> O terceiro dígito (dezena) é MENOR QUE 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos3 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo3 = 2
            
            elif dica == 4: 
                #posição da unidade
                # Verificação do intervalo para evitar a repetição de dicas
                if -3 < pos4 < 0:
                    #determina o tipo da dica
                    tipo = randint(1, 2)
                    print(f'\nTipo: {tipo}\n')
                    # dica de par ou ímpar
                    if tipo == 1 and tipo4 != 1:
                        #identifica se é par e mostra para o usuário
                        if unidade % 2 == 0:
                            print('==> O Quarto dígito (unidade) é PAR!!')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos4 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo4 = 1
                        #caso não for --> mostra para o usuário que é ímpar
                        else:
                            print('==> O Quarto dígito (unidade) é ÍMPAR!! ')
                            # Decresce a posição para indicar que uma dica já foi dada
                            pos4 -= 1
                            # Determina que esse tipo de dica já foi dado
                            tipo4 = 1
                    #dica do número ser maior ou igual a cinco ou número menor que cinco
                    else:
                        if tipo4 != 2:
                            #se a unidade for maior ou igual a cinco
                            if unidade >= 5:
                                print('==> O Quarto dígito (unidade) é maior ou igual a 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos4 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo4 = 2
                            #se a unidade for menor que cinco
                            else:
                                print('==> O Quarto dígito (unidade) é menor que 5!!')
                                # Decresce a posição para indicar que uma dica já foi dada
                                pos4 -= 1
                                # Determina que esse tipo de dica já foi dado
                                tipo4 = 2
                    
                    

        # Resetando contador de acertos
        # acertos = 0
        cont += 1

    # Mensagem de finalização do jogo
    if venceu == 1:
        print(f'\n\t>=<>=<>=< PARABÉNS >=<>=<>=<\nVocê acertou o <<CÓDIGO SECRETO>> na {cont}ª tentativa.')
    else:
        print(f'\nNão foi dessa vez :(\nO <<CÓDIGO SECRETO>> era {numGerado}\nMas não se preocupe, você pode jogar de novo!\n')

    # print('-' * 60)
    
    # Perguntar se o usuário deseja jogar novamente
    jogar = int(input('\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÃO\n\n>> '))
    while jogar not in [0, 1]:
        jogar = int(input('\nOpção inválida\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÃO\n\n>> '))  

# Mensagem de encerramento
print('\n\t=-=-=-=-= Muito obrigado por jogar!! =-=-=-=-=')