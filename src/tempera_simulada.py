import math
from random import random
from mochila import vizinho_aleatorio, fitness

TEMPERATURA_INICIAL = 1000 # valor inicial definido arbitrariamente
ALPHA = 0.95 # testar resultados com diferentes valores de alpha

# instancia é uma config. completa do problema da mochila (i.e., uma combinação de itens com um peso e um valor)
# estado é a representão binária da instancia
# t_max é o número máximo de interações caso o usuário não o defina
def tempera_simulada(instancia, estado, t_max = 100_000_000):
    for t in range (1, t_max):
        temp = escalonamento(t)

        if temp==0.1: # (valor mínimo diferente de zero definido arbitrariamente)
            return estado # a temperatura foi esgotada e o melhor estado possível encontrado

        candidato = vizinho_aleatorio(estado)

        # a diferença dos valores de fitness que diz qual combinação é mais desejável
        deltaenerg = fitness(candidato, instancia) - fitness(estado, instancia)

        if deltaenerg > 0:
            estado = candidato # esse candidato se provou a melhor opção
        else:
            # se passar na probabilidade (como se girando um dado), escolhe a pior opção
            if random() < probabilidade(temp, deltaenerg):
                estado = candidato

# função de relação entre o tempo t e a “temperatura” T (essa função controla a probabilidade de aceitar passos piores)
def escalonamento(t):
    return TEMPERATURA_INICIAL * (ALPHA ** t) # decresce geometricamente

# calculo da probabilidade dado por: eˆ(∆E/T)
def probabilidade(temp, deltaenerg):
    return pow(math.e, deltaenerg/temp)

