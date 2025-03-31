# Controladores principais
jogar = cont = 1
# Números que serão verificados
numGerado = aux = 1234
numPalpite = 0
# Controladores da existência de dicas
dica1 = dica2 = dica3 = dica4 = 0
# Controladores da exibição das posições
pos1 = pos2 = pos3 = pos4 = '__'
# Controladores de acertos e vitórias
acertos = venceu = 0

# Desmembramento do número gerado
milhar = aux//1000
aux -= milhar*1000
centena = aux//100
aux -= centena*100
dezena = aux//10
aux -= dezena*10
unidade = aux

# Looping para continuar jogando
while jogar == 1:
    print('\n\t=-=-=-=-= BEM VINDO(A) AO JOGO SECRETO =-=-=-=-=\n\n')
    print('Você tem 10 tentaivas para acertar o número secreto entre [1000 e 9999]\n')
    print('A partir da 5ª tentativa, o jogo irá te ajudar com dicas.\n\tBoa sorte!!')
    avanco = input('\n\t<< Tecle Enter para continuar >>')

    print('-'*60)
    # Palpite inicial
    aux = numPalpite = int(input("\n\t>> 1ª Tentativa <<\n\nDigite seu palpite: "))

    # Looping da advinhação
    while cont < 10:

        # Verificação de vitória (perguntar sobre palpites que completam a sequência mas mostram um código incorreto)
        if numPalpite != numGerado: #Caso negativo -> o número não corresponde
            # Desmembramento do número recebido
            milhar2 = aux//1000
            aux -= milhar2*1000
            centena2 = aux//100
            aux -= centena2*100
            dezena2 = aux//10
            aux -= dezena2*10
            unidade2 = aux

            # Início das validações -> dicas pendentes
            # Comparação do 1º dígito
            if pos1 == '__':
                if milhar == milhar2:
                    pos1 = milhar2
                    acertos += 1
                else:
                    pos1 = '__'

            # Comparação do 2º dígito
            if pos2 == '__':
                if centena == centena2:
                    pos2 = centena2
                    acertos += 1
                else:
                    pos2 = '__'
            
            # Comparação do 3º dígito
            if pos3 == '__':
                if dezena == dezena2:
                    pos3 = dezena2
                    acertos += 1
                else:
                    pos3 = '__'

            # Comparação do 4º dígito
            if pos4 == '__':
                if unidade == unidade2:
                    pos4 = unidade2
                    acertos += 1
                else:
                    pos4 = '__'

            #Exibição
            print(f'\nVocê acertou {acertos} dígito(s) dessa vez...')
            print(f'\nSeu código atual é: {pos1} {pos2} {pos3} {pos4}')

            # Incrementos e decrementos
            acertos = 0
            cont += 1

            # Leitura do palpite subsequente
            aux = numPalpite = int(input(f"\n\t>> {cont}ª Tentativa <<\nDigite seu palpite: "))
        else: #Caso positivo -> o número corresponde
            venceu = 1
            break

        # Verificação da vitória
        if venceu == 0:
            print(f'\nNão foi dessa vez :(\nO <<CÓDIGO SECRETO>> era {numGerado}\nMas não se preocupe, você pode jogar de novo!\n')
        else:
            print(f'\n\t>=<>=<>=< PARABÉNS >=<>=<>=<\nVocê acertou o <<CÓDIGO SECRETO>> na {cont}ª tentaiva.')

        print('-'*60)
    
    # Confirmação de continuidade do jogo
    jogar = int(input('\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÂO\n\n>> '))
    while jogar != 1 and jogar !=0:
        jogar = int(input('\nOpção inválida\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÂO\n\n>> '))  

# Mensagem de encerramento
print('\n\t=-=-=-=-= Muito obrigado por jogar!! =-=-=-=-=')