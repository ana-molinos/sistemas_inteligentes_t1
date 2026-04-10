import matplotlib.pyplot as plt
import pandas as pd


def plotar_convergencia_ts(historico, caminho_saida):
    plt.figure()
    plt.plot(historico)
    plt.title("Convergência - Têmpera Simulada")
    plt.xlabel("iteração")
    plt.ylabel("fitness")
    plt.tight_layout()
    plt.savefig(caminho_saida)
    plt.close()


def plotar_convergencia_ag(historico_melhor, historico_media, caminho_saida):
    plt.figure()
    plt.plot(historico_melhor, label="melhor")
    plt.plot(historico_media, label="média")
    plt.title("Convergência - Algoritmo Genético")
    plt.xlabel("geração")
    plt.ylabel("fitness")
    plt.legend()
    plt.tight_layout()
    plt.savefig(caminho_saida)
    plt.close()


def plotar_comparacao(historico_ts, historico_ag, caminho_saida):
    plt.figure()
    x_ts = [i / len(historico_ts) for i in range(len(historico_ts))]
    x_ag = [i / len(historico_ag) for i in range(len(historico_ag))]
    plt.plot(x_ts, historico_ts, label="têmpera simulada")
    plt.plot(x_ag, historico_ag, label="algoritmo genético")
    plt.title("Comparação de Convergência")
    plt.xlabel("progresso normalizado")
    plt.ylabel("fitness")
    plt.legend()
    plt.tight_layout()
    plt.savefig(caminho_saida)
    plt.close()


def exportar_csv(resultados, caminho_saida):
    pd.DataFrame(resultados).to_csv(caminho_saida, index=False)
