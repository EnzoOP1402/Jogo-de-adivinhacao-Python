jogar = 1
numGerado = aux = 1234
numPalpite = 0

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

    # Looping da advinhação
    
    
    jogar = int(input('\nDeseja jogar novamente?\n[1] - SIM\n[0] - NÂO\n\n>> '))

print('\nMuito obrigado por jogar!!')