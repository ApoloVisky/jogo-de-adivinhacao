print("##################################")
print("Bem vindo ao jogo de adivinhação!")
print("##################################")

import  random
numero_secreto = random.randrange(1,101) #gera um numero aleatorio de 1 a 100
numero_tentativas = 3
rodada = 1
pontos = 1000

## Definindo o nível de dificuldade

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = str(input("Defina o nível: "))

if nivel == "1":
    numero_tentativas = 20

elif nivel == 2:
    numero_tentativas = 10

else :
    numero_tentativas = 5



for rodada in range(1, numero_tentativas +1):

    print("Rodada ",rodada, " de", numero_tentativas) #printa o numero de tentativas restantes


    chute_str = input("Digite um número de 1 a 100:")
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve escolher um número entre 1 e 100")
        continue


    chute_str = int(chute_str)
    maior = numero_secreto < chute_str
    menor = numero_secreto > chute_str

    if numero_secreto == chute_str:
        print("Você acertou!")  #caso acerte o numero
        break
    else:
        print("Você errou!")  #caso erre o numero

        if (menor):
            print("O seu chute foi menor que o número secreto!")

        elif (maior):
            print("O seu chute foi maior que o número secreto!")

            pontos = pontos - abs(numero_secreto - chute_str)




    rodada = rodada + 1
print("Você fez ", pontos, " pontos")
print("Fim do jogo!")
#aula 116