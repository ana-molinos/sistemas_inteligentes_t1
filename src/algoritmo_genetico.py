# Algoritmo Genético (AG) para o Problema da Mochila
#
# RESPONSABILIDADE DESTE MÓDULO:
#   - Inicializar a população (conjunto de soluções binárias)
#   - Implementar seleção (ex: torneio ou roleta)
#   - Implementar crossover (ex: ponto único ou dois pontos sobre o vetor binário)
#   - Implementar mutação (flip aleatório de bits — mesma operação de vizinhança da TS)
#   - Implementar a substituição geracional (ex: elitismo)
#   - Registrar o histórico de fitness do melhor e da média da população por geração
#
# ONDE A MODELAGEM APARECE AQUI:
#   - Cromossomo: vetor binário de SolucaoMochila (mesmo da TS)
#   - Fitness: mesma função de SolucaoMochila.fitness()
#   - Crossover: opera diretamente sobre a representação binária dos itens
#   - Mutação: flip de bits — análoga ao vizinho_aleatorio() da TS
#   - Soluções inviáveis: mesma estratégia de penalização do módulo TS
#
# PARÂMETROS DO ALGORITMO (a definir com base em experimentos):
#   - tamanho_populacao: número de indivíduos
#   - num_geracoes: critério de parada
#   - taxa_crossover: probabilidade de crossover entre dois pais
#   - taxa_mutacao: probabilidade de flip de cada bit
#   - tipo_selecao: torneio | roleta
#   - elitismo: bool — preserva o melhor indivíduo entre gerações
#
# VARIANTE ESCOLHIDA: AG Canônico
#   - Seleção por torneio ou roleta (configurável)
#   - Crossover de ponto único ou dois pontos (configurável)
#   - Mutação por flip de bit com taxa_mutacao por gene
#   - Substituição geracional com elitismo opcional
#
# JUSTIFICATIVA DO AG CANÔNICO:
#   - Estrutura clássica e bem documentada — facilita as justificativas do artigo
#   - O crossover sobre vetor binário é a operação mais natural para esta representação
#   - Comparação direta com TS é mais limpa: ambos usam a mesma representação e fitness


def algoritmo_genetico(instancia, parametros):
    pass
