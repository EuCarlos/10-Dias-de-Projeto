from random import randint

print('='*70)
print('-'*20 + 'JOGO DE ADIVINHAÇÃO DE NÚMEROS' + '-'*20)
print('='*70)
print('Selecionamos um número aleatório entre 1 e 100. Veja se consegue adivinhá-lo em 10 tentativas ou menos. \nInformaremos se sua estimativa foi muito alta ou muito baixa.\n')
NumAleatorio = randint(1,100)
Bool = True
cont = 0

while (Bool == True):
    Palpite = int(input('Insira uma estimativa: '))
    if(Palpite == NumAleatorio):
        print('\033[42mParabéns! Você acertou!\033[0;0m')
        Bool = False
    else:
        if(Palpite > NumAleatorio):
            print('O último palpite foi muito alto! Tente mais um numero.')
            cont += 1
            if cont == 10:
                Bool = False
                print('\033[41mErrou! Suas tentativas acabaram!\033[0;0m')
        else:
            print('A última estimativa foi muito baixa! Tente mais um numero.')
            cont += 1
            if cont == 10:
                Bool = False
                print('\033[41mErrou! Suas tentativas acabaram!\033[0;0m')
