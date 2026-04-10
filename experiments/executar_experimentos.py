# Script de execução dos experimentos comparativos
#
# RESPONSABILIDADE DESTE MÓDULO:
#   - Executar TS e AG sobre as mesmas instâncias com os mesmos seeds
#   - Rodar múltiplas execuções (ex: 30 rodadas) para análise estatística
#   - Coletar: melhor solução, tempo de execução, fitness médio, desvio padrão
#   - Chamar os módulos de visualização para gerar os gráficos
#
# EXPERIMENTOS PLANEJADOS:
#   1. Instância pequena: comparar com solução ótima (força bruta)
#   2. Instância média/grande: comparar TS vs AG (qualidade + tempo)
#   3. Sensibilidade de parâmetros: variar alpha (TS) e taxa_mutacao (AG)
#
# MÉTRICAS DE COMPARAÇÃO:
#   - Qualidade da solução: fitness obtido (e gap para o ótimo, quando conhecido)
#   - Velocidade de convergência: iterações até estabilizar
#   - Consistência: desvio padrão entre execuções


def executar_experimento_ts(instancia, parametros, n_rodadas):
    pass


def executar_experimento_ag(instancia, parametros, n_rodadas):
    pass


def comparar_algoritmos(instancia, parametros_ts, parametros_ag, n_rodadas):
    pass


if __name__ == "__main__":
    pass
