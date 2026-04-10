import time
import statistics
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.mochila import gerar_estado_inicial, fitness
from src.tempera_simulada import tempera_simulada
from src.algoritmo_genetico import algoritmo_genetico
from src.visualizacao import plotar_convergencia_ts, plotar_convergencia_ag, plotar_comparacao, exportar_csv
from data.instancias import gerar_instancia_pequena, gerar_instancia_media, gerar_instancia_grande, forca_bruta


def executar_experimento_ts(instancia, n_rodadas=30):
    resultados = []
    for _ in range(n_rodadas):
        inicio = time.time()
        estado, historico = tempera_simulada(instancia, gerar_estado_inicial(instancia))
        tempo = time.time() - inicio
        resultados.append({"fitness": fitness(estado, instancia), "tempo": tempo, "historico": historico})
    return resultados


def executar_experimento_ag(instancia, n_rodadas=30):
    resultados = []
    for _ in range(n_rodadas):
        inicio = time.time()
        melhor, historico_melhor, historico_media = algoritmo_genetico(instancia)
        tempo = time.time() - inicio
        resultados.append({"fitness": fitness(melhor, instancia), "tempo": tempo, "historico": historico_melhor})
    return resultados


def comparar_algoritmos(instancia, n_rodadas=30, prefixo=""):
    print("executando têmpera simulada...")
    res_ts = executar_experimento_ts(instancia, n_rodadas)

    print("executando algoritmo genético...")
    res_ag = executar_experimento_ag(instancia, n_rodadas)

    fitness_ts = [r["fitness"] for r in res_ts]
    fitness_ag = [r["fitness"] for r in res_ag]
    tempos_ts  = [r["tempo"]   for r in res_ts]
    tempos_ag  = [r["tempo"]   for r in res_ag]

    print(f"\n{'':>30} {'TS':>10} {'AG':>10}")
    print(f"{'melhor fitness':>30} {max(fitness_ts):>10} {max(fitness_ag):>10}")
    print(f"{'média fitness':>30} {statistics.mean(fitness_ts):>10.2f} {statistics.mean(fitness_ag):>10.2f}")
    print(f"{'desvio padrão fitness':>30} {statistics.stdev(fitness_ts):>10.2f} {statistics.stdev(fitness_ag):>10.2f}")
    print(f"{'tempo médio (s)':>30} {statistics.mean(tempos_ts):>10.4f} {statistics.mean(tempos_ag):>10.4f}")

    melhor_ts = max(res_ts, key=lambda r: r["fitness"])
    melhor_ag = max(res_ag, key=lambda r: r["fitness"])

    plotar_convergencia_ts(melhor_ts["historico"], f"resultados/{prefixo}convergencia_ts.png")
    plotar_convergencia_ag(melhor_ag["historico"], melhor_ag["historico"], f"resultados/{prefixo}convergencia_ag.png")
    plotar_comparacao(melhor_ts["historico"], melhor_ag["historico"], f"resultados/{prefixo}comparacao.png")

    exportar_csv(
        [{"algoritmo": "ts", "fitness": r["fitness"], "tempo": r["tempo"]} for r in res_ts] +
        [{"algoritmo": "ag", "fitness": r["fitness"], "tempo": r["tempo"]} for r in res_ag],
        f"resultados/{prefixo}resultados.csv"
    )
    print(f"\ngráficos e CSV salvos em resultados/")


if __name__ == "__main__":
    print("=== instância pequena ===")
    inst = gerar_instancia_pequena()
    _, otimo = forca_bruta(inst)
    print(f"ótimo por força bruta: {otimo}")
    comparar_algoritmos(inst, n_rodadas=30, prefixo="pequena_")

    print("\n=== instância média ===")
    comparar_algoritmos(gerar_instancia_media(), n_rodadas=30, prefixo="media_")

    print("\n=== instância grande ===")
    comparar_algoritmos(gerar_instancia_grande(), n_rodadas=30, prefixo="grande_")
