# -*- coding: utf-8 -*-
"""exerPy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14q_CJpEwrvNGidC9niZhQdXciQd6GXFQ
"""

def fase1(posicao1, posicao2):
 if (posicao1 == 3):
    print("O rato não pode ficar perto do gato! GAME OVER")
 elif (posicao1 == 6):
   print("Parabéns! Passou de fase!")
 elif (posicao2 == 6):
    print("O gato não pode ficar perto do rato! GAME OVER")
 elif (posicao2 == 3):
   print("Parabéns! Passou de fase!")
 else:
   print("Posição ocupada!")


print("Bem vindos a fase 1!")
print()
print("Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos. \nO rato não deve ficar perto do gato:")
print()
print(" *  *  _  G ")
print(" R  _  *  * ")




posicaoRato = int(input("Em qual posição quer alocar o RATO?"))
posicaoGato = int(input("Em qual posição quer alocar o GATO?"))
fase1(posicaoRato, posicaoGato)

#alogoritmo do código:
# imprimir na tela a apresentação do jogo;
# perguntar ao jogador em qual posição deseja alocar;
## se posição desocupada
# então preenher posição
# enquanto não preencher as duas...

print("     HOTEL DOS ANIMAIS")
print("Especificando posição:")
print([1,2,3,4])
print([5,6,7,8])
print()

#Fase 1
print("Bem vindos a fase 1!")
print()
print("Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos. \nO rato não deve ficar perto do gato:")
print()
print(" *  *  _  G ")
print(" R  _  *  * ")

hotel=[['*', '*', '_', 'G'], ['R', '_', '*', '*']] #mapa da fase
 

posicaoRato = int(input("Em qual posição quer alocar o RATO?"))
posicaoGato = int(input("Em qual posição quer alocar o GATO?"))

if posicaoGato != 3 and posicaoRato != 6: #Condição de derrota
    print("Game over!!")
    exit()
else:
    print("Parabéns! Desbloqueou a fase2") #Condição de vitória

#fase 2
print("Bem vindos a fase 2!")
print()
print("Na Fase 2, o cão não pode ficar ao lado do osso.:")
print()
print(" - * * *")
print(" * C - - ")

hotel=[['-', '*', '*', '*'], ['*', 'C', '-', '-']] #mapa da fase

posicaoCao = int(input("Em qual posição quer alocar o CÃO?"))
posicaoCao = int(input("Em qual posição quer alocar o CÃO?"))
posicaoOsso = int(input("Em qual posição quer alocar o OSSO?"))

if posicaoCao != 7 and posicaoCao != 8 and posicaoOsso != 1: #Condição de derrota
    print("Game over!!")
    exit()
else:
    print("Parabéns! Desbloqueou a fase3") #Condição de vitória

#Fase 3
print("Bem vindos a fase 3!")

print("Na Fase 3, o jogador deve alocar o GATO, RATO e OSSO seguinte matriz que representa os quartos:")
hotel=[['-', '*', '*', '*'], ['-', 'G', '-', '*']] #mapa da fase
print(hotel)
posicaoGato = int(input("Em qual posição quer alocar o GATO?"))
posicaoRato = int(input("Em qual posição quer alocar o RATO?"))
posicaoOsso = int(input("Em qual posição quer alocar o OSSO?"))

if posicaoGato != 7 and posicaoRato != 1 and posicaoOsso != 5: #Condição de derrota
     print("Game over!!")
     exit()
else:
     print("Parabéns! Desbloqueou a fase4") #Condição de vitória


#Fase 4
print(input("Bem vindos a fase 4!"))
print("Na Fase 2, o jogador deve alocar o QUEIJO, QUEIJO e OSSO seguinte matriz que representa os quartos:")
hotel = [['-', '-', '-', '*'], ['*', 'R', '*', '*']]  # mapa da fase
print(hotel)
posicaoQueijo = int(input("Em qual posição quer alocar o QUEIJO?"))
posicaoQueijo = int(input("Em qual posição quer alocar o QUEIJO?"))
posicaoOsso = int(input("Em qual posição quer alocar o OSSO?"))

if posicaoQueijo != 1 and posicaoQueijo != 3 and posicaoOsso != 2:  # Condição de derrota
     print("Game over!!")
     exit()
else:
     print("Você ganhou!")  # Condição de vitória


#Fase 4
print(input("Bem vindos a fase 4!"))
print("Na Fase 2, o jogador deve alocar o QUEIJO, QUEIJO e OSSO seguinte matriz que representa os quartos:")
hotel = [['-', '-', '-', '*'], ['*', 'R', '*', '*']]  # mapa da fase
print(hotel)
posicaoQueijo = int(input("Em qual posição quer alocar o QUEIJO?"))
posicaoQueijo = int(input("Em qual posição quer alocar o QUEIJO?"))
posicaoOsso = int(input("Em qual posição quer alocar o OSSO?"))

if posicaoQueijo != 1 and posicaoQueijo != 3 and posicaoOsso != 2:  # Condição de derrota
     print("Game over!!")
     exit()
else:
     print("Você ganhou!")  # Condição de vitória"""
