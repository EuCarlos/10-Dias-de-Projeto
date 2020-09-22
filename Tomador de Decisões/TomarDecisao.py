#_*_ coding: utf-8 _*_
import random

def gerarDecisao():
    decisaoGerada = random.choice(respostas)
    print(decisaoGerada)

Script = open('scriptBot.txt')
respostas = Script.readlines()

print('='*70)
print('-'*24,'Github.com/EuCarlos/','-'*24)
print('='*70)

Loop = 'S'
while Loop == 'S':
    Pergunta = str(input('O Que você quer que eu decida por você? \n'))
    gerarDecisao()
    Loop = str(input('Deseja fazer mais uma pergunta? [S/N]'))
    if Loop == 'N':
        print('Fim das perguntas!')
