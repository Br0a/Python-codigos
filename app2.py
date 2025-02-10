import random

# Lista de palavras para o jogo
palavras = ['maçã', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    # Escolhe uma palavra aleatória da lista
    palavra = random.choice(palavras)
    # Cria uma lista para armazenar as letras corretas
    letras_corretas = ['_'] * len(palavra)
    # Cria uma lista para armazenar as letras erradas
    letras_erradas = []
    # Define o número de tentativas
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Você tem 6 tentativas para adivinhar a palavra.")

    while tentativas > 0 and '_' in letras_corretas:
        # Mostra a palavra com as letras corretas
        print(' '.join(letras_corretas))
        # Pede ao usuário para digitar uma letra
        letra = input("Digite uma letra: ").lower()
        # Verifica se a letra é correta
        if letra in palavra:
            #  Substitui as letras corretas na lista
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_corretas[i] = letra
        else:
            # Adiciona a letra errada á lista
            letras_erradas.append(letra)
            # Diminui o número de tentativas
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")
            print(f"Letras erradas: {', '.join(letras_erradas)}")
    # Verifica se o usuário ganhou ou perdeu
    if '_' not in letras_corretas:
        print("Parabéns! Você ganhou!")
    else:
        print(f"Você perdeu! A palavra era {palavra}.")

# Inicia o jogo
jogo_da_forca()
