import random


def escolha():
    while True:
        numero = int(input(
        'ESCOLHA UMA CATEGORIA:\n'
        '[0] - Animais\n'
        '[1] - Cidades\n'
        '[2] - Esportes\n'
        '[3] - Paises\n'
        '[4] - Comida\n'
        '[5] - Linguagem de Programação '))
        if numero < 0 or numero > 5:
            print('OPÇÃO INVALIDA')
        else:
            return numero


def palavra(numero):
    escolha = ''

    animais = ['capivara', 'tubarao', 'cachorro', 'gato', 'hipopotamo', 'baleia']
    cidades = ['natal', 'fortaleza', 'recife', 'salvador', 'maceio', 'teresina']
    esportes = ['futebol', 'basquete', 'volei', 'criquete', 'xadrez', 'judo']
    paises = ['brasil', 'argentina', 'japao', 'china', 'inglaterra', 'alemanha']
    comida = ['lasanha', 'frango', 'feijao', 'arroz', 'pipoca', 'pizza']
    linguagem_de_programacao = ['python', 'javascript', 'java', 'ruby', 'julia', 'php', 'c']

    if numero == 0:
        escolha = random.choice(animais)
    elif numero == 1:
        escolha = random.choice(cidades)
    elif numero == 2:
        escolha = random.choice(esportes)
    elif numero == 3:
        escolha = random.choice(paises)
    elif numero == 4:
        escolha = random.choice(comida)
    elif numero == 5:
        escolha = random.choice(linguagem_de_programacao)

    return escolha


if __name__ == '__main__':

    x = escolha()
    n = palavra(x)
    print(n)
