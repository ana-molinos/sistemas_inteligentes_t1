import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.mochila import Item, InstanciaMochila, SolucaoMochila, fitness

SEED_PEQUENA = 42
SEED_MEDIA   = 42
SEED_GRANDE  = 42


def gerar_instancia_aleatoria(n_itens, fracao_capacidade=0.5, seed=None):
    rng = random.Random(seed)
    itens = [Item(rng.randint(1, 20), rng.randint(1, 20)) for _ in range(n_itens)]
    capacidade = int(sum(item.peso for item in itens) * fracao_capacidade)
    return InstanciaMochila(itens, capacidade)


def gerar_instancia_pequena():
    return gerar_instancia_aleatoria(10, seed=SEED_PEQUENA)


def gerar_instancia_media():
    return gerar_instancia_aleatoria(30, seed=SEED_MEDIA)


def gerar_instancia_grande():
    return gerar_instancia_aleatoria(100, seed=SEED_GRANDE)


def forca_bruta(instancia):
    melhor_solucao = None
    melhor_fitness = -1

    for i in range(2 ** instancia.n):
        genes = [(i >> j) & 1 for j in range(instancia.n)]
        solucao = SolucaoMochila(genes)
        valor = fitness(solucao, instancia)
        if valor > melhor_fitness:
            melhor_fitness = valor
            melhor_solucao = solucao

    return melhor_solucao, melhor_fitness
