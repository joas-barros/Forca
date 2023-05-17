import escolha_da_palavra as sexo
from time import sleep


x = 'JOGO DA FORCA'
z = '='*len(x)
print(f'=={z}==')
print(f'  {x}')
print(f'=={z}==')

numero = sexo.escolha()
palavra = sexo.palavra(numero)
sleep(1)
print('palavra escolhida')
print('loading...')
sleep(3)

letras_usuario = list()
chances = 6
ganhou = False

while True:
    # criar a lógica
    for letra in palavra:
        if letra in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print(f'Voce tem {chances} chances')
    tentativa = input('Escolha uma letra para advinhar: ').strip().lower()
    letras_usuario.append(tentativa)
    if tentativa not in palavra:
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'Parabéns, voce ganhou. A palavra era: {palavra}')
else:
    print(f'Voce perdeu! A palavra era {palavra}')
