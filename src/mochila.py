# Definição formal do Problema da Mochila (0/1 Knapsack)
#
# RESPONSABILIDADE DESTE MÓDULO:
#   - Representar uma instância do problema (lista de itens + capacidade)
#   - Representar uma solução (vetor binário)
#   - Calcular o fitness (valor total) e verificar viabilidade (peso <= capacidade)
#   - Gerar o estado inicial (solução inicial)
#   - Gerar um vizinho aleatório (flip de um bit) — operação de vizinhança compartilhada
#
# MODELAGEM:
#   - Cada item i tem peso w_i e valor v_i
#   - Uma solução é um vetor x ∈ {0,1}^n onde x_i=1 significa "item i está na mochila"
#   - Função objetivo: maximizar Σ(v_i * x_i) sujeito a Σ(w_i * x_i) <= capacidade
#
# JUSTIFICATIVA DA REPRESENTAÇÃO BINÁRIA:
#   - Diretamente mapeada para a natureza 0/1 do problema (incluir ou não cada item)
#   - Operação de vizinhança natural: flip de um bit (troca inclusão/exclusão de um item)
#   - Compatível com ambos os algoritmos: TS usa flip individual, AG usa crossover sobre bits


class Item:
    pass


class InstanciaMochila:
    pass


class SolucaoMochila:
    pass
