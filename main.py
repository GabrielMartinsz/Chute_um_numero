import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input("Chute um número de 1 a 10:"))
  if chute > valor_aleatorio:
    print('Chute foi acima')
  elif chute < valor_aleatorio:
    print('Chute foi abaixo')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você acertou!')