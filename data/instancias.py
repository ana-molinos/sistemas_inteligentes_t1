# Instâncias do Problema da Mochila para os experimentos
#
# RESPONSABILIDADE DESTE MÓDULO:
#   - Definir instâncias fixas (pequena, média, grande) para testes reproduzíveis
#   - Implementar gerador de instâncias aleatórias (para experimentos estatísticos)
#
# INSTÂNCIAS: todas geradas aleatoriamente com seed fixo (reprodutibilidade)
#   - PEQUENA: ~10 itens — permite verificar solução ótima por força bruta (2^10 = 1024)
#   - MÉDIA:   ~30 itens — custo moderado
#   - GRANDE:  ~100 itens — onde a busca heurística se justifica
#
# FORMATO DE CADA INSTÂNCIA:
#   {
#     "nome": str,
#     "capacidade": int,
#     "itens": [{"peso": int, "valor": int}, ...]
#   }
#
# CAPACIDADE SUGERIDA: ~50% da soma total dos pesos (instância com tensão real)
# SEEDS FIXOS: garantem que TS e AG rodam sobre exatamente os mesmos dados
#
# NOTA: Para a instância pequena, será calculado o ótimo por força bruta
# e usado como referência para medir a qualidade das heurísticas no artigo.

SEED_PEQUENA = 42
SEED_MEDIA   = 42
SEED_GRANDE  = 42


def gerar_instancia_aleatoria(n_itens, fracao_capacidade=0.5, seed=None):
    # fracao_capacidade: fração da soma total de pesos usada como capacidade
    pass


def gerar_instancia_pequena():
    pass


def gerar_instancia_media():
    pass


def gerar_instancia_grande():
    pass


def forca_bruta(instancia):
    # Enumera todas as 2^n soluções — só viável para instância pequena
    pass
