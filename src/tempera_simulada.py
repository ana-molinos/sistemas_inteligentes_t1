# Têmpera Simulada para o Problema da Mochila
#
# RESPONSABILIDADE DESTE MÓDULO:
#   - Implementar o laço principal da Têmpera Simulada
#   - Implementar a função de escalonamento de temperatura
#   - Implementar o critério de aceitação de soluções piores: P = e^(ΔE / T)
#   - Registrar o histórico de fitness a cada iteração (para plotar convergência)
#
# ONDE A MODELAGEM APARECE AQUI:
#   - Estado: instância de SolucaoMochila (vetor binário)
#   - Vizinho: gerado via vizinho_aleatorio() do módulo mochila (flip de 1 bit)
#   - Fitness: calculado via SolucaoMochila.fitness()
#   - ΔE = fitness(candidato) - fitness(estado_atual)
#   - Soluções inviáveis (peso > capacidade): tratadas com penalização no fitness
#
# PARÂMETROS DO ALGORITMO (ambos os critérios de parada são configuráveis):
# 
#   - max_iteracoes: limite de iterações (critério de parada por contagem)
#
# CRITÉRIO DE PARADA: para quando T <= 0 OU iteração > max_iteracoes
# (o que vier primeiro)
#
# ESCOLHA DA FUNÇÃO DE ESCALONAMENTO:
#   - Resfriamento geométrico: T(t) = temperatura_inicial * alpha^t  (mais comum, previsível)
#   - Outras opções: logarítmico, linear — a justificativa será feita no artigo

import math
from random import random
from mochila import vizinho_aleatorio, fitness

TEMPERATURA_INICIAL = 1000 # valor inicial definido arbitrariamente
ALPHA = 0.95 # testar resultados com diferentes valores de alpha

def tempera_simulada(instancia, estado, t_max = 100_000_000):
    for t in range (1, t_max):
        temp = escalonamento(t)

        if temp==0.1: # (valor mínimo diferente de zero definido arbitrariamente)
            return estado

        candidato = vizinho_aleatorio(instancia)

        deltaenerg = fitness(candidato) - fitness(estado)

        if deltaenerg > 0:
            estado = candidato
        else:
            if random() < probabilidade(temp, deltaenerg):
                estado = candidato

def escalonamento(t):
    return TEMPERATURA_INICIAL * (ALPHA ** t) # decresce geometricamente

def probabilidade(temp, deltaenerg):
    return pow(math.e, deltaenerg/temp)

