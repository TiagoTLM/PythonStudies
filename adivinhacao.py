'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep #Apenas para passar uma ideia de que o computador "demorou" para pensar em um número
#Atribuindo os valores de 0 - 5 à variável para que o computador possa escolher um aleatório.

#lista = [0,1,2,3,4,5] usei esta variável pq estava utilizando o método random.choice(). Depois mudei para o método randint(0,5)
sorteio = randint(0, 5)
#print(sorteio) Apenas um teste para ver se deu certo até aqui
print('Vou pensar em um número de 0 até 5...')
print('Pesando...')
sleep(2)
num = int(input('Em que número estou pensando? '))

#Inicio das condições para definir e o usuário escolheu o numero certo
if num == sorteio:
    print('Parabéns, você escolheu o número certo! {}'.format(sorteio))
else:
    print('Que pena, você errou... {}'.format(sorteio))    