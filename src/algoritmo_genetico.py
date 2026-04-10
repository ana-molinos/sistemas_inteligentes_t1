import random
from src.mochila import SolucaoMochila, gerar_estado_inicial, fitness

TAMANHO_POPULACAO = 50
NUM_GERACOES = 500
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.02  # probabilidade de flip por gene

def algoritmo_genetico(instancia, num_geracoes=NUM_GERACOES):
    populacao = [gerar_estado_inicial(instancia) for _ in range(TAMANHO_POPULACAO)]
    historico_melhor = []
    historico_media = []

    for _ in range(num_geracoes):
        populacao = sorted(populacao, key=lambda s: fitness(s, instancia), reverse=True)

        valores = [fitness(s, instancia) for s in populacao]
        historico_melhor.append(valores[0])
        historico_media.append(sum(valores) / len(valores))

        nova_populacao = [populacao[0]]  # elitismo: preserva o melhor

        while len(nova_populacao) < TAMANHO_POPULACAO:
            pai1 = selecao_torneio(populacao, instancia)
            pai2 = selecao_torneio(populacao, instancia)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho1))
            nova_populacao.append(mutacao(filho2))

        populacao = nova_populacao[:TAMANHO_POPULACAO]

    melhor = max(populacao, key=lambda s: fitness(s, instancia))
    return melhor, historico_melhor, historico_media

def selecao_torneio(populacao, instancia, k=3):
    # seleciona k individuos aleatórios e retorna o melhor
    competidores = random.sample(populacao, k)
    return max(competidores, key=lambda s: fitness(s, instancia))

def crossover(pai1, pai2):
    # crossover de ponto unico
    if random.random() > TAXA_CROSSOVER:
        return pai1, pai2
    ponto = random.randint(1, len(pai1.genes) - 1)
    genes1 = pai1.genes[:ponto] + pai2.genes[ponto:]
    genes2 = pai2.genes[:ponto] + pai1.genes[ponto:]
    return SolucaoMochila(genes1), SolucaoMochila(genes2)

def mutacao(solucao):
    # flip de cada gene com probabilidade taxa mutacao
    genes = [1 - g if random.random() < TAXA_MUTACAO else g for g in solucao.genes]
    return SolucaoMochila(genes)
