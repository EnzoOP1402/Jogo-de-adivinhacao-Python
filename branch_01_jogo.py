# from random import randint
# numGerado = randint(1000,9999)

# Número secreto fixo
numGerado = 1234
# Desmembramento do número gerado
milhar = numGerado // 1000
centena = (numGerado % 1000) // 100
dezena = (numGerado % 100) // 10
unidade = numGerado % 10

# numGrado = 5678
# milhar = 5
# centena = 6
# dezena = 7
# unidade = 8

# Loop principal do jogo
jogar = 1

while jogar == 1:
    # Resetando variáveis para uma nova rodada
    cont = 1
    venceu = 0
    acertos = 0
    pos1 = pos2 = pos3 = pos4 = -1

    # Introdução do jogo
    print('\n\t=-=-=-=-= BEM VINDO(A) AO JOGO SECRETO =-=-=-=-=\n\n')
    print('Você tem 10 tentativas para acertar o número secreto entre [1000 e 9999]\n')
    print("Caso você acerte a posição e o número o jogo irá manter ele e informar que está correto!")
    print('A partir da 5ª tentativa, o jogo irá te ajudar com dicas.\n\tBoa sorte!!')
    input('\n\t<< Tecle Enter para continuar >>')

    print('-' * 60)

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
        if pos1 == -1 and milhar == milhar2:
            pos1 = milhar2
            acertos += 1
        if pos2 == -1 and centena == centena2:
            pos2 = centena2
            acertos += 1
        if pos3 == -1 and dezena == dezena2:
            pos3 = dezena2
            acertos += 1
        if pos4 == -1 and unidade == unidade2:
            pos4 = unidade2
            acertos += 1

        # Exibição do resultado da tentativa
        print(f'\nVocê acertou {acertos} dígito(s) dessa vez...')
        print('\nSeu código atual é: ', end='')
        if pos1 == -1:
            print('__', end=' ')
        else:
            print(pos1, end=' ')
        if pos2 == -1:
            print('__', end=' ')
        else:
            print(pos2, end=' ')
        if pos3 == -1:
            print('__', end=' ')
        else:
            print(pos3, end=' ')
        if pos4 == -1:
            print('__', end=' ')
        else:
            print(pos4, end=' ')

        # Esboço da ideia da dicas
        # if cont == 5:
        #     num = num2 =0
        #     # Gera um número aleatório entre 1 e 4
        #     if num == 1:
        #         if pos1 == -1:
        #             # Gera outro número aleatório
        #             # Se for 1 -> verifica se é par ou impar -> imprime
        #             # S for 2 -> verifica se é maior ou igual a 5 -> imprime na posição
        #             num = 0


        # Resetando contador de acertos
        acertos = 0
        cont += 1

    # Mensagem de finalização do jogo
    if venceu == 1:
        print(f'\n\t>=<>=<>=< PARABÉNS >=<>=<>=<\nVocê acertou o <<CÓDIGO SECRETO>> na {cont}ª tentativa.')
    else:
        print(f'\nNão foi dessa vez :(\nO <<CÓDIGO SECRETO>> era {numGerado}\nMas não se preocupe, você pode jogar de novo!\n')

    print('-' * 60)
    
    # Perguntar se o usuário deseja jogar novamente
    jogar = int(input('\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÃO\n\n>> '))
    while jogar not in [0, 1]:
        jogar = int(input('\nOpção inválida\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÃO\n\n>> '))  

# Mensagem de encerramento
print('\n\t=-=-=-=-= Muito obrigado por jogar!! =-=-=-=-=')