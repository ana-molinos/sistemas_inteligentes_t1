import random
import copy

class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

class InstanciaMochila:
    def __init__(self, itens, capacidade):
        self.itens = itens       # lista de itens
        self.capacidade = capacidade
        self.n = len(itens)

class SolucaoMochila:
    def __init__(self, genes):
        self.genes = genes       # vetor binário 

def gerar_estado_inicial(instancia):
    # solução inicial aleatória
    genes = [random.randint(0, 1) for _ in range(instancia.n)]
    return SolucaoMochila(genes)

# estado = solução (binário) / instancia = problema
def fitness(estado, instancia):
    
    # testando se o resultado obedece a capacidade da mochila
    if sum(gene * Item.peso for gene, item in zip(estado.genes, instancia.itens)) > instancia.capacidade
        return 0
    
    # retorna o somatório do valor dos itens
    return sum(gene * Item.valor for gene, item in zip(estado.genes, instancia.itens))

# implementa um flip aleatório no vetor (i.e.: troca dois itens de estado de pertencimento a mochila)
# isso é válido pois a abordagem da tempera simulada é baseada em aleatorização da solução
def vizinho_aleatorio(estado):
    candidato = copy.copy(estado.genes)      # copia o vetor atual
    i = random.randint(0, len(candidato)-1)  # escolhe um índice aleatório                                                                                        
    candidato[i] = 1 - candidato[i]          # inversão (flip)                                                                                                
    return SolucaoMochila(candidato) 
