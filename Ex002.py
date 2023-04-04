# Exercício 002: Crie um algoritmo que peça o nome do usuário e após receber, imprima na tela uma mensagem de boas vindas.
# Criação da variável "nome", logo após criar eu já utilizo o método Input para salvar um valor (string) na variável.

nome = input('Por favor, informe o seu nome: ')
# Utilizei o método Format "{}" para inserir o nome salvo na variável dentro da mensagem enviada pelo programa
print('Boas vindas {}!'.format(nome))
