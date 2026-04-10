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
#   - temperatura_inicial: temperatura inicial
#   - temperatura_final: temperatura mínima (critério de parada por temperatura)
#   - max_iteracoes: limite de iterações (critério de parada por contagem)
#   - alpha: fator de resfriamento (ex: T <- T * alpha, resfriamento geométrico)
#   - iteracoes_por_temperatura: quantas trocas tentar antes de baixar a temperatura
#
# CRITÉRIO DE PARADA: para quando T < temperatura_final OU iteração > max_iteracoes
# (o que vier primeiro) — ambos configuráveis via parametros
#
# ESCOLHA DA FUNÇÃO DE ESCALONAMENTO:
#   - Resfriamento geométrico: T(t) = temperatura_inicial * alpha^t  (mais comum, previsível)
#   - Outras opções: logarítmico, linear — a justificativa será feita no artigo


def tempera_simulada(instancia, parametros):
    pass
