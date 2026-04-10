from src.mochila import Item, InstanciaMochila, gerar_estado_inicial, fitness
from src.tempera_simulada import tempera_simulada
from src.algoritmo_genetico import algoritmo_genetico
from data.instancias import gerar_instancia_pequena, forca_bruta

instancia = gerar_instancia_pequena()

_, otimo = forca_bruta(instancia)
print("ótimo por força bruta:", otimo)

print(f"capacidade máxima: {instancia.capacidade}")
for i, item in enumerate(instancia.itens):
    print(f"  item {i}: peso={item.peso}, valor={item.valor}")

estado = gerar_estado_inicial(instancia)
resultado_ts = tempera_simulada(instancia, estado)

print("\ntêmpera simulada:")
for i, (gene, item) in enumerate(zip(resultado_ts.genes, instancia.itens)):
    status = "dentro" if gene == 1 else "fora"
    print(f"  item {i} (peso={item.peso}, valor={item.valor}) → {status}")
peso_ts = sum(gene * item.peso for gene, item in zip(resultado_ts.genes, instancia.itens))
print(f"fitness: {fitness(resultado_ts, instancia)} | peso total: {peso_ts}/{instancia.capacidade}")

resultado_ag = algoritmo_genetico(instancia)

print("\nalgoritmo genético:")
for i, (gene, item) in enumerate(zip(resultado_ag.genes, instancia.itens)):
    status = "dentro" if gene == 1 else "fora"
    print(f"  item {i} (peso={item.peso}, valor={item.valor}) → {status}")
peso_ag = sum(gene * item.peso for gene, item in zip(resultado_ag.genes, instancia.itens))
print(f"fitness: {fitness(resultado_ag, instancia)} | peso total: {peso_ag}/{instancia.capacidade}")
