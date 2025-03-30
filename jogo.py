jogar = cont = 1
numGerado = aux = 1234
numPalpite = 0
dica1 = dica2 = dica3 = dica4 = 0

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
    while cont <= 10:

        # Verificação de vitória
        if numPalpite != numGerado:
            print('Perdeu')
            # Desmembramento do número recebido
            milhar2 = aux//1000
            aux -= milhar2*1000
            centena2 = aux//100
            aux -= centena2*100
            dezena2 = aux//10
            aux -= dezena2*10
            unidade = aux

            # Adicionar o início das validações: dicas e exibição do código

            cont += 1
            aux = numPalpite = int(input(f"\n\t>> {cont}ª Tentativa <<\nDigite seu palpite: "))
        else:
            print('Venceu')
            break
    
    jogar = int(input('\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÂO\n\n>> '))
    while jogar != 1 and jogar !=0:
        jogar = int(input('\nOpção inválida\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÂO\n\n>> '))  

print('\n\t=-=-=-=-= Muito obrigado por jogar!! =-=-=-=-=')